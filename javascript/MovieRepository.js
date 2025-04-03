const AWS = require('aws-sdk');
const logger = require('./logger');

/**
 * Encapsulates an Amazon DynamoDB table of movie data.
 */
class MovieRepository {
    /**
     * Constructor for MovieRepository.
     * @param {AWS.DynamoDB.DocumentClient} docClient - A DynamoDB DocumentClient. If null, a new client will be created.
     * @param {string} tableName - The name of the table. Defaults to "Movies".
     */
    constructor(docClient = null, tableName = 'Movies') {
        this.docClient = docClient || new AWS.DynamoDB.DocumentClient();
        this.dynamoDB = new AWS.DynamoDB();
        this.tableName = tableName;
    }

    /**
     * Determines whether a table exists.
     * @param {string} tableName - The name of the table to check.
     * @returns {Promise<boolean>} True when the table exists; otherwise, False.
     */
    async exists(tableName) {
        try {
            await this.dynamoDB.describeTable({ TableName: tableName }).promise();
            return true;
        } catch (err) {
            if (err.code === 'ResourceNotFoundException') {
                return false;
            }
            logger.error(`Couldn't check for existence of ${tableName}. Error: ${err.message}`);
            throw err;
        }
    }

    /**
     * Creates an Amazon DynamoDB table that can be used to store movie data.
     * @param {string} tableName - The name of the table to create.
     * @returns {Promise<AWS.DynamoDB.Table>} The newly created table.
     */
    async createTable(tableName) {
        try {
            const params = {
                TableName: tableName,
                KeySchema: [
                    { AttributeName: 'year', KeyType: 'HASH' },  // Partition key
                    { AttributeName: 'title', KeyType: 'RANGE' }  // Sort key
                ],
                AttributeDefinitions: [
                    { AttributeName: 'year', AttributeType: 'N' },
                    { AttributeName: 'title', AttributeType: 'S' }
                ],
                ProvisionedThroughput: {
                    ReadCapacityUnits: 10,
                    WriteCapacityUnits: 10
                }
            };

            const table = await this.dynamoDB.createTable(params).promise();
            await this.dynamoDB.waitFor('tableExists', { TableName: tableName }).promise();
            return table;
        } catch (err) {
            logger.error(`Couldn't create table ${tableName}. Error: ${err.message}`);
            throw err;
        }
    }

    /**
     * Lists the Amazon DynamoDB tables for the current account.
     * @returns {Promise<string[]>} The list of tables.
     */
    async listTables() {
        try {
            const result = await this.dynamoDB.listTables().promise();
            result.TableNames.forEach(table => console.log(table));
            return result.TableNames;
        } catch (err) {
            logger.error(`Couldn't list tables. Error: ${err.message}`);
            throw err;
        }
    }

    /**
     * Adds a movie to the table.
     * @param {string} title - The title of the movie.
     * @param {number} year - The release year of the movie.
     * @param {string} plot - The plot summary of the movie.
     * @param {number} rating - The quality rating of the movie.
     * @returns {Promise<void>}
     */
    async insert(title, year, plot, rating) {
        try {
            const params = {
                TableName: this.tableName,
                Item: {
                    year: year,
                    title: title,
                    info: {
                        plot: plot,
                        rating: rating
                    }
                }
            };

            await this.docClient.put(params).promise();
        } catch (err) {
            logger.error(`Couldn't add movie ${title} to table ${this.tableName}. Error: ${err.message}`);
            throw err;
        }
    }

    /**
     * Gets movie data from the table for a specific movie.
     * @param {string} title - The title of the movie.
     * @param {number} year - The release year of the movie.
     * @returns {Promise<Object>} The data about the requested movie.
     */
    async select(title, year) {
        try {
            const params = {
                TableName: this.tableName,
                Key: {
                    year: year,
                    title: title
                }
            };

            const result = await this.docClient.get(params).promise();
            return result.Item;
        } catch (err) {
            logger.error(`Couldn't get movie ${title} from table ${this.tableName}. Error: ${err.message}`);
            throw err;
        }
    }

    /**
     * Updates rating and plot data for a movie in the table.
     * @param {string} title - The title of the movie to update.
     * @param {number} year - The release year of the movie to update.
     * @param {string} plot - The updated plot summary to give the movie.
     * @param {number} rating - The updated rating to give the movie.
     * @returns {Promise<Object>} The fields that were updated, with their new values.
     */
    async update(title, year, plot, rating) {
        try {
            const params = {
                TableName: this.tableName,
                Key: {
                    year: year,
                    title: title
                },
                UpdateExpression: 'set info.rating = :r, info.plot = :p',
                ExpressionAttributeValues: {
                    ':r': rating,
                    ':p': plot
                },
                ReturnValues: 'UPDATED_NEW'
            };

            const result = await this.docClient.update(params).promise();
            return result.Attributes;
        } catch (err) {
            logger.error(`Couldn't update movie ${title} in table ${this.tableName}. Error: ${err.message}`);
            throw err;
        }
    }

    /**
     * Queries for movies that were released in the specified year.
     * @param {number} year - The year to query.
     * @returns {Promise<Object[]>} The list of movies that were released in the specified year.
     */
    async queryMovies(year) {
        try {
            const params = {
                TableName: this.tableName,
                KeyConditionExpression: '#yr = :yyyy',
                ExpressionAttributeNames: {
                    '#yr': 'year'
                },
                ExpressionAttributeValues: {
                    ':yyyy': year
                }
            };

            const result = await this.docClient.query(params).promise();
            return result.Items;
        } catch (err) {
            logger.error(`Couldn't query for movies released in ${year}. Error: ${err.message}`);
            throw err;
        }
    }

    /**
     * Scans for movies that were released in a range of years.
     * @param {Object} yearRange - The range of years to retrieve.
     * @param {number} yearRange.first - The first year in the range.
     * @param {number} yearRange.second - The second year in the range.
     * @returns {Promise<Object[]>} The list of movies released in the specified years.
     */
    async scanMovies(yearRange) {
        try {
            const params = {
                TableName: this.tableName,
                FilterExpression: '#yr between :start_yr and :end_yr',
                ExpressionAttributeNames: {
                    '#yr': 'year'
                },
                ExpressionAttributeValues: {
                    ':start_yr': yearRange.first,
                    ':end_yr': yearRange.second
                },
                ProjectionExpression: '#yr, title, info.rating'
            };

            const movies = [];
            let result;
            do {
                result = await this.docClient.scan(params).promise();
                movies.push(...result.Items);
                params.ExclusiveStartKey = result.LastEvaluatedKey;
            } while (result.LastEvaluatedKey);

            return movies;
        } catch (err) {
            logger.error(`Couldn't scan for movies. Error: ${err.message}`);
            throw err;
        }
    }

    /**
     * Deletes a movie from the table.
     * @param {string} title - The title of the movie to delete.
     * @param {number} year - The release year of the movie to delete.
     * @returns {Promise<void>}
     */
    async delete(title, year) {
        try {
            const params = {
                TableName: this.tableName,
                Key: {
                    year: year,
                    title: title
                }
            };

            await this.docClient.delete(params).promise();
        } catch (err) {
            logger.error(`Couldn't delete movie ${title}. Error: ${err.message}`);
            throw err;
        }
    }

    /**
     * Deletes the table.
     * @returns {Promise<void>}
     */
    async deleteTable() {
        try {
            await this.dynamoDB.deleteTable({ TableName: this.tableName }).promise();
            await this.dynamoDB.waitFor('tableNotExists', { TableName: this.tableName }).promise();
        } catch (err) {
            logger.error(`Couldn't delete table. Error: ${err.message}`);
            throw err;
        }
    }

    /**
     * Writes a batch of movies to the table.
     * @param {Object[]} movies - The list of movies to write.
     * @returns {Promise<void>}
     */
    async writeBatch(movies) {
        try {
            const batchSize = 25; // DynamoDB batch write limit
            for (let i = 0; i < movies.length; i += batchSize) {
                const batch = movies.slice(i, i + batchSize);
                const params = {
                    RequestItems: {
                        [this.tableName]: batch.map(movie => ({
                            PutRequest: {
                                Item: movie
                            }
                        }))
                    }
                };

                let result = await this.docClient.batchWrite(params).promise();

                // Handle unprocessed items
                while (Object.keys(result.UnprocessedItems).length > 0) {
                    params.RequestItems = result.UnprocessedItems;
                    result = await this.docClient.batchWrite(params).promise();
                }
            }
        } catch (err) {
            logger.error(`Couldn't load data into table ${this.tableName}. Error: ${err.message}`);
            throw err;
        }
    }
}

module.exports = MovieRepository;
