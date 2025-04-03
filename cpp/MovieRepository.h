#pragma once

#include <aws/core/Aws.h>
#include <aws/dynamodb/DynamoDBClient.h>
#include <aws/dynamodb/model/AttributeValue.h>
#include <string>
#include <vector>
#include <map>
#include <memory>

namespace AmazonQCustomizationDemo {

/**
 * @brief Encapsulates an Amazon DynamoDB table of movie data.
 */
class MovieRepository {
public:
    /**
     * @brief Constructor for MovieRepository.
     * @param clientConfig Configuration for the DynamoDB client. If null, default configuration is used.
     * @param tableName The name of the table. Defaults to "Movies".
     */
    MovieRepository(const Aws::Client::ClientConfiguration* clientConfig = nullptr, 
                   const std::string& tableName = "Movies");
    
    /**
     * @brief Destructor.
     */
    ~MovieRepository();

    /**
     * @brief Determines whether a table exists.
     * @param tableName The name of the table to check.
     * @return True when the table exists; otherwise, False.
     */
    bool Exists(const std::string& tableName);

    /**
     * @brief Creates an Amazon DynamoDB table that can be used to store movie data.
     * @param tableName The name of the table to create.
     * @return True if the table was created successfully; otherwise, False.
     */
    bool CreateTable(const std::string& tableName);

    /**
     * @brief Lists the Amazon DynamoDB tables for the current account.
     * @return The list of table names.
     */
    std::vector<std::string> ListTables();

    /**
     * @brief Adds a movie to the table.
     * @param title The title of the movie.
     * @param year The release year of the movie.
     * @param plot The plot summary of the movie.
     * @param rating The quality rating of the movie.
     * @return True if the movie was added successfully; otherwise, False.
     */
    bool Insert(const std::string& title, int year, const std::string& plot, double rating);

    /**
     * @brief Gets movie data from the table for a specific movie.
     * @param title The title of the movie.
     * @param year The release year of the movie.
     * @return The data about the requested movie as a map of attribute names to values.
     */
    std::map<std::string, Aws::DynamoDB::Model::AttributeValue> Select(const std::string& title, int year);

    /**
     * @brief Updates rating and plot data for a movie in the table.
     * @param title The title of the movie to update.
     * @param year The release year of the movie to update.
     * @param plot The updated plot summary to give the movie.
     * @param rating The updated rating to the give the movie.
     * @return True if the movie was updated successfully; otherwise, False.
     */
    bool Update(const std::string& title, int year, const std::string& plot, double rating);

    /**
     * @brief Queries for movies that were released in the specified year.
     * @param year The year to query.
     * @return The list of movies that were released in the specified year.
     */
    std::vector<std::map<std::string, Aws::DynamoDB::Model::AttributeValue>> QueryMovies(int year);

    /**
     * @brief Scans for movies that were released in a range of years.
     * @param firstYear The first year in the range.
     * @param secondYear The second year in the range.
     * @return The list of movies released in the specified years.
     */
    std::vector<std::map<std::string, Aws::DynamoDB::Model::AttributeValue>> ScanMovies(int firstYear, int secondYear);

    /**
     * @brief Deletes a movie from the table.
     * @param title The title of the movie to delete.
     * @param year The release year of the movie to delete.
     * @return True if the movie was deleted successfully; otherwise, False.
     */
    bool Delete(const std::string& title, int year);

    /**
     * @brief Deletes the table.
     * @return True if the table was deleted successfully; otherwise, False.
     */
    bool DeleteTable();

    /**
     * @brief Writes a batch of movies to the table.
     * @param movies The list of movies to write.
     * @return True if the batch was written successfully; otherwise, False.
     */
    bool WriteBatch(const std::vector<std::map<std::string, Aws::DynamoDB::Model::AttributeValue>>& movies);

private:
    std::shared_ptr<Aws::DynamoDB::DynamoDBClient> m_dynamoDbClient;
    std::string m_tableName;
};

} // namespace AmazonQCustomizationDemo
