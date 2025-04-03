import * as AWS from 'aws-sdk';
import { DocumentClient } from 'aws-sdk/clients/dynamodb';

/**
 * Interface for movie data
 */
interface MovieInfo {
  plot: string;
  rating: number;
}

/**
 * Interface for movie item
 */
interface Movie {
  year: number;
  title: string;
  info: MovieInfo;
}

/**
 * Interface for year range
 */
interface YearRange {
  first: number;
  second: number;
}

/**
 * Encapsulates an Amazon DynamoDB table of movie data.
 */
export class MovieRepository {
  private docClient: DocumentClient;
  private dynamoDB: AWS.DynamoDB;
  private tableName: string;

  /**
   * Constructor for MovieRepository.
   * @param docClient - A DynamoDB DocumentClient. If null, a new client will be created.
   * @param tableName - The name of the table. Defaults to "Movies".
   */
  constructor(docClient?: DocumentClient, tableName: string = 'Movies') {
    this.docClient = docClient || new AWS.DynamoDB.DocumentClient();
    this.dynamoDB = new AWS.DynamoDB();
    this.tableName = tableName;
  }

  /**
   * Determines whether a table exists.
   * @param tableName - The name of the table to check.
   * @returns True when the table exists; otherwise, False.
   */
  async exists(tableName: string): Promise<boolean> {
    try {
      await this.dynamoDB.describeTable({ TableName: tableName }).promise();
      return true;
    } catch (err) {
      if (err.code === 'ResourceNotFoundException') {
        return false;
      }
      console.error(`Couldn't check for existence of ${tableName}. Error: ${err.message}`);
      throw err;
    }
  }

  /**
   * Creates an Amazon DynamoDB table that can be used to store movie data.
   * @param tableName - The name of the table to create.
   * @returns The newly created table.
   */
  async createTable(tableName: string): Promise<AWS.DynamoDB.CreateTableOutput> {
    try {
      const params: AWS.DynamoDB.CreateTableInput = {
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
      console.error(`Couldn't create table ${tableName}. Error: ${err.message}`);
      throw err;
    }
  }

  /**
   * Lists the Amazon DynamoDB tables for the current account.
   * @returns The list of tables.
   */
  async listTables(): Promise<string[]> {
    try {
      const result = await this.dynamoDB.listTables().promise();
      result.TableNames?.forEach(table => console.log(table));
      return result.TableNames || [];
    } catch (err) {
      console.error(`Couldn't list tables. Error: ${err.message}`);
      throw err;
    }
  }

  /**
   * Adds a movie to the table.
   * @param title - The title of the movie.
   * @param year - The release year of the movie.
   * @param plot - The plot summary of the movie.
   * @param rating - The quality rating of the movie.
   */
  async insert(title: string, year: number, plot: string, rating: number): Promise<void> {
    try {
      const params: DocumentClient.PutItemInput = {
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
      console.error(`Couldn't add movie ${title} to table ${this.tableName}. Error: ${err.message}`);
      throw err;
    }
  }

  /**
   * Gets movie data from the table for a specific movie.
   * @param title - The title of the movie.
   * @param year - The release year of the movie.
   * @returns The data about the requested movie.
   */
  async select(title: string, year: number): Promise<Movie | undefined> {
    try {
      const params: DocumentClient.GetItemInput = {
        TableName: this.tableName,
        Key: {
          year: year,
          title: title
        }
      };

      const result = await this.docClient.get(params).promise();
      return result.Item as Movie;
    } catch (err) {
      console.error(`Couldn't get movie ${title} from table ${this.tableName}. Error: ${err.message}`);
      throw err;
    }
  }

  /**
   * Updates rating and plot data for a movie in the table.
   * @param title - The title of the movie to update.
   * @param year - The release year of the movie to update.
   * @param plot - The updated plot summary to give the movie.
   * @param rating - The updated rating to give the movie.
   * @returns The fields that were updated, with their new values.
   */
  async update(title: string, year: number, plot: string, rating: number): Promise<DocumentClient.AttributeMap> {
    try {
      const params: DocumentClient.UpdateItemInput = {
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
      return result.Attributes || {};
    } catch (err) {
      console.error(`Couldn't update movie ${title} in table ${this.tableName}. Error: ${err.message}`);
      throw err;
    }
  }

  /**
   * Queries for movies that were released in the specified year.
   * @param year - The year to query.
   * @returns The list of movies that were released in the specified year.
   */
  async queryMovies(year: number): Promise<Movie[]> {
    try {
      const params: DocumentClient.QueryInput = {
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
      return (result.Items || []) as Movie[];
    } catch (err) {
      console.error(`Couldn't query for movies released in ${year}. Error: ${err.message}`);
      throw err;
    }
  }

  /**
   * Scans for movies that were released in a range of years.
   * @param yearRange - The range of years to retrieve.
   * @returns The list of movies released in the specified years.
   */
  async scanMovies(yearRange: YearRange): Promise<Movie[]> {
    try {
      const params: DocumentClient.ScanInput = {
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

      const movies: Movie[] = [];
      let result: DocumentClient.ScanOutput;
      
      do {
        result = await this.docClient.scan(params).promise();
        movies.push(...(result.Items || []) as Movie[]);
        params.ExclusiveStartKey = result.LastEvaluatedKey;
      } while (result.LastEvaluatedKey);

      return movies;
    } catch (err) {
      console.error(`Couldn't scan for movies. Error: ${err.message}`);
      throw err;
    }
  }

  /**
   * Deletes a movie from the table.
   * @param title - The title of the movie to delete.
   * @param year - The release year of the movie to delete.
   */
  async delete(title: string, year: number): Promise<void> {
    try {
      const params: DocumentClient.DeleteItemInput = {
        TableName: this.tableName,
        Key: {
          year: year,
          title: title
        }
      };

      await this.docClient.delete(params).promise();
    } catch (err) {
      console.error(`Couldn't delete movie ${title}. Error: ${err.message}`);
      throw err;
    }
  }

  /**
   * Deletes the table.
   */
  async deleteTable(): Promise<void> {
    try {
      await this.dynamoDB.deleteTable({ TableName: this.tableName }).promise();
      await this.dynamoDB.waitFor('tableNotExists', { TableName: this.tableName }).promise();
    } catch (err) {
      console.error(`Couldn't delete table. Error: ${err.message}`);
      throw err;
    }
  }

  /**
   * Writes a batch of movies to the table.
   * @param movies - The list of movies to write.
   */
  async writeBatch(movies: Movie[]): Promise<void> {
    try {
      const batchSize = 25; // DynamoDB batch write limit
      for (let i = 0; i < movies.length; i += batchSize) {
        const batch = movies.slice(i, i + batchSize);
        const params: DocumentClient.BatchWriteItemInput = {
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
        while (result.UnprocessedItems && Object.keys(result.UnprocessedItems).length > 0) {
          params.RequestItems = result.UnprocessedItems;
          result = await this.docClient.batchWrite(params).promise();
        }
      }
    } catch (err) {
      console.error(`Couldn't load data into table ${this.tableName}. Error: ${err.message}`);
      throw err;
    }
  }
}
