#include <iostream>
#include <aws/core/Aws.h>
#include <aws/dynamodb/DynamoDBClient.h>
#include <aws/dynamodb/model/DeleteItemRequest.h>
#include <aws/dynamodb/model/GetItemRequest.h>
#include <aws/dynamodb/model/AttributeValue.h>
#include "MovieRepository.h"

/**
 * Example demonstrating how to delete a movie from DynamoDB using the MovieRepository class
 * 
 * This example shows:
 * 1. Creating a MovieRepository instance
 * 2. Checking if a movie exists
 * 3. Deleting the movie if it exists
 */
int main()
{
    // Initialize the AWS SDK
    Aws::SDKOptions options;
    Aws::InitAPI(options);
    
    {
        // Create a MovieRepository instance
        MovieRepository movies;
        
        // Confirm that the movie exists in the database
        auto movie = movies.Select(
            "Crawlspace",    // title
            2016        // year
        );
        
        if (movie.has_value()) {
            // Delete the movie
            // This demonstrates how to remove an item from DynamoDB
            std::cout << "Deleting movie" << std::endl;
            bool success = movies.Delete(
                "Crawlspace",    // title
                2016        // year
            );
            
            if (success) {
                std::cout << "Movie deleted successfully" << std::endl;
            } else {
                std::cout << "Failed to delete movie" << std::endl;
            }
        } else {
            // Warn that the movie doesn't exist
            std::cout << "Movie not found; therefore, no need to delete it." << std::endl;
        }
    }
    
    // Shutdown the AWS SDK
    Aws::ShutdownAPI(options);
    return 0;
}
