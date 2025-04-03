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
            "Death Race",    // title
            2008        // year
        );
        
        if (movie.has_value()) {
            // The movie was found, so update it
            // This demonstrates how to update an existing item in DynamoDB
            bool success = movies.Update(
                "Death Race",    // title
                2008,       // year
                "Ex-con Jensen Ames is forced by the warden of a notorious prison to compete in our post-industrial world's most popular sport: a car race in which inmates must brutalize and kill one another on the road to victory.",     // plot
                6.4      // rating
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
