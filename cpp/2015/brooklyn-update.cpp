#include <iostream>
#include <aws/core/Aws.h>
#include <aws/dynamodb/DynamoDBClient.h>
#include <aws/dynamodb/model/UpdateItemRequest.h>
#include <aws/dynamodb/model/GetItemRequest.h>
#include <aws/dynamodb/model/AttributeValue.h>
#include "MovieRepository.h"

/**
 * Example demonstrating how to update a movie in DynamoDB using the MovieRepository class
 * 
 * This example shows:
 * 1. Creating a MovieRepository instance
 * 2. Checking if a movie exists
 * 3. Updating the movie's attributes if it exists
 */
int main()
{
    // Initialize the AWS SDK
    Aws::SDKOptions options;
    Aws::InitAPI(options);
    
    {
        // Create a MovieRepository instance
        MovieRepository movies;
        
        // Check if the movie exists
        auto movie = movies.Select(
            "Brooklyn",    // title
            2015        // year
        );
        
        if (movie.has_value()) {
            // The movie was found, so update it
            // This demonstrates how to update an existing item in DynamoDB
            bool success = movies.Update(
                "Brooklyn",    // title
                2015,       // year
                "An Irish immigrant lands in 1950s Brooklyn, where she quickly falls into a romance with a local. When her past catches up with her, however, she must choose between two countries and the lives that exist within.",     // plot
                7.5      // rating
            );
            
            if (success) {
                std::cout << "Movie updated successfully" << std::endl;
            } else {
                std::cout << "Failed to update movie" << std::endl;
            }
        } else {
            // The movie was not found, so we cannot update
            std::cout << "Movie not found" << std::endl;
        }
    }
    
    // Shutdown the AWS SDK
    Aws::ShutdownAPI(options);
    return 0;
}
