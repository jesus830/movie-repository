using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using Amazon.DynamoDBv2;
using Amazon.DynamoDBv2.Model;
using Amazon.DynamoDBv2.DocumentModel;
using System.Linq;

namespace AmazonQCustomizationDemo
{
    /// <summary>
    /// Encapsulates an Amazon DynamoDB table of movie data.
    /// </summary>
    public class MovieRepository
    {
        private readonly IAmazonDynamoDB _dynamoDbClient;
        private Table _table;
        private readonly string _tableName;

        /// <summary>
        /// Constructor for MovieRepository.
        /// </summary>
        /// <param name="dynamoDbClient">A DynamoDB client. If null, a new client will be created.</param>
        /// <param name="tableName">The name of the table. Defaults to "Movies".</param>
        public MovieRepository(IAmazonDynamoDB dynamoDbClient = null, string tableName = "Movies")
        {
            _dynamoDbClient = dynamoDbClient ?? new AmazonDynamoDBClient();
            _tableName = tableName;
            
            // Check if the table exists
            if (Exists(tableName).Result)
            {
                _table = Table.LoadTable(_dynamoDbClient, tableName);
            }
        }

        /// <summary>
        /// Determines whether a table exists.
        /// </summary>
        /// <param name="tableName">The name of the table to check.</param>
        /// <returns>True when the table exists; otherwise, False.</returns>
        public async Task<bool> Exists(string tableName)
        {
            try
            {
                var response = await _dynamoDbClient.DescribeTableAsync(new DescribeTableRequest
                {
                    TableName = tableName
                });
                
                _table = Table.LoadTable(_dynamoDbClient, tableName);
                return true;
            }
            catch (ResourceNotFoundException)
            {
                return false;
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error checking if table exists: {ex.Message}");
                throw;
            }
        }

        /// <summary>
        /// Creates an Amazon DynamoDB table that can be used to store movie data.
        /// </summary>
        /// <param name="tableName">The name of the table to create.</param>
        /// <returns>The newly created table.</returns>
        public async Task<Table> CreateTable(string tableName)
        {
            try
            {
                var request = new CreateTableRequest
                {
                    TableName = tableName,
                    KeySchema = new List<KeySchemaElement>
                    {
                        new KeySchemaElement
                        {
                            AttributeName = "year",
                            KeyType = "HASH" // Partition key
                        },
                        new KeySchemaElement
                        {
                            AttributeName = "title",
                            KeyType = "RANGE" // Sort key
                        }
                    },
                    AttributeDefinitions = new List<AttributeDefinition>
                    {
                        new AttributeDefinition
                        {
                            AttributeName = "year",
                            AttributeType = "N"
                        },
                        new AttributeDefinition
                        {
                            AttributeName = "title",
                            AttributeType = "S"
                        }
                    },
                    ProvisionedThroughput = new ProvisionedThroughput
                    {
                        ReadCapacityUnits = 10,
                        WriteCapacityUnits = 10
                    }
                };

                var response = await _dynamoDbClient.CreateTableAsync(request);

                // Wait until the table is active
                bool isTableActive = false;
                while (!isTableActive)
                {
                    var tableStatus = await _dynamoDbClient.DescribeTableAsync(tableName);
                    isTableActive = tableStatus.Table.TableStatus == "ACTIVE";
                    if (!isTableActive)
                        await Task.Delay(1000);
                }

                _table = Table.LoadTable(_dynamoDbClient, tableName);
                return _table;
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Couldn't create table {tableName}. Error: {ex.Message}");
                throw;
            }
        }

        /// <summary>
        /// Lists the Amazon DynamoDB tables for the current account.
        /// </summary>
        /// <returns>The list of tables.</returns>
        public async Task<List<string>> ListTables()
        {
            try
            {
                var response = await _dynamoDbClient.ListTablesAsync();
                foreach (var table in response.TableNames)
                {
                    Console.WriteLine(table);
                }
                return response.TableNames;
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Couldn't list tables. Error: {ex.Message}");
                throw;
            }
        }

        /// <summary>
        /// Adds a movie to the table.
        /// </summary>
        /// <param name="title">The title of the movie.</param>
        /// <param name="year">The release year of the movie.</param>
        /// <param name="plot">The plot summary of the movie.</param>
        /// <param name="rating">The quality rating of the movie.</param>
        public async Task Insert(string title, int year, string plot, decimal rating)
        {
            try
            {
                var movie = new Document
                {
                    ["year"] = year,
                    ["title"] = title,
                    ["info"] = new Document
                    {
                        ["plot"] = plot,
                        ["rating"] = rating
                    }
                };

                await _table.PutItemAsync(movie);
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Couldn't add movie {title} to table {_tableName}. Error: {ex.Message}");
                throw;
            }
        }

        /// <summary>
        /// Gets movie data from the table for a specific movie.
        /// </summary>
        /// <param name="title">The title of the movie.</param>
        /// <param name="year">The release year of the movie.</param>
        /// <returns>The data about the requested movie.</returns>
        public async Task<Document> Select(string title, int year)
        {
            try
            {
                return await _table.GetItemAsync(year, title);
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Couldn't get movie {title} from table {_tableName}. Error: {ex.Message}");
                throw;
            }
        }

        /// <summary>
        /// Updates rating and plot data for a movie in the table.
        /// </summary>
        /// <param name="title">The title of the movie to update.</param>
        /// <param name="year">The release year of the movie to update.</param>
        /// <param name="plot">The updated plot summary to give the movie.</param>
        /// <param name="rating">The updated rating to the give the movie.</param>
        /// <returns>The fields that were updated, with their new values.</returns>
        public async Task<Document> Update(string title, int year, string plot, decimal rating)
        {
            try
            {
                var key = new Dictionary<string, DynamoDBEntry>
                {
                    ["year"] = year,
                    ["title"] = title
                };

                var updates = new UpdateItemOperationConfig
                {
                    ReturnValues = ReturnValues.UpdatedNewAttributes
                };

                var updateExpression = new Expression();
                updateExpression.SetAttribute("info.rating", rating);
                updateExpression.SetAttribute("info.plot", plot);

                return await _table.UpdateItemAsync(key, updateExpression, updates);
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Couldn't update movie {title} in table {_tableName}. Error: {ex.Message}");
                throw;
            }
        }

        /// <summary>
        /// Queries for movies that were released in the specified year.
        /// </summary>
        /// <param name="year">The year to query.</param>
        /// <returns>The list of movies that were released in the specified year.</returns>
        public async Task<List<Document>> QueryMovies(int year)
        {
            try
            {
                var filter = new QueryFilter("year", QueryOperator.Equal, year);
                var search = _table.Query(filter);

                var results = new List<Document>();
                do
                {
                    var documents = await search.GetNextSetAsync();
                    results.AddRange(documents);
                }
                while (!search.IsDone);

                return results;
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Couldn't query for movies released in {year}. Error: {ex.Message}");
                throw;
            }
        }

        /// <summary>
        /// Scans for movies that were released in a range of years.
        /// </summary>
        /// <param name="firstYear">The first year in the range.</param>
        /// <param name="secondYear">The second year in the range.</param>
        /// <returns>The list of movies released in the specified years.</returns>
        public async Task<List<Document>> ScanMovies(int firstYear, int secondYear)
        {
            try
            {
                var filter = new ScanFilter();
                filter.AddCondition("year", ScanOperator.Between, firstYear, secondYear);

                var search = _table.Scan(filter);

                var results = new List<Document>();
                do
                {
                    var documents = await search.GetNextSetAsync();
                    results.AddRange(documents);
                }
                while (!search.IsDone);

                return results;
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Couldn't scan for movies. Error: {ex.Message}");
                throw;
            }
        }

        /// <summary>
        /// Deletes a movie from the table.
        /// </summary>
        /// <param name="title">The title of the movie to delete.</param>
        /// <param name="year">The release year of the movie to delete.</param>
        public async Task Delete(string title, int year)
        {
            try
            {
                await _table.DeleteItemAsync(year, title);
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Couldn't delete movie {title}. Error: {ex.Message}");
                throw;
            }
        }

        /// <summary>
        /// Deletes the table.
        /// </summary>
        public async Task DeleteTable()
        {
            try
            {
                var request = new DeleteTableRequest
                {
                    TableName = _tableName
                };

                await _dynamoDbClient.DeleteTableAsync(request);
                _table = null;
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Couldn't delete table. Error: {ex.Message}");
                throw;
            }
        }

        /// <summary>
        /// Writes a batch of movies to the table.
        /// </summary>
        /// <param name="movies">The list of movies to write.</param>
        public async Task WriteBatch(List<Document> movies)
        {
            try
            {
                var batchWrite = _table.CreateBatchWrite();
                
                foreach (var movie in movies)
                {
                    batchWrite.AddDocumentToPut(movie);
                }

                await batchWrite.ExecuteAsync();
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Couldn't load data into table {_tableName}. Error: {ex.Message}");
                throw;
            }
        }
    }
}
