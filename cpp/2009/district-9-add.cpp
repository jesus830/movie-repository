#include <iostream>
#include <aws/core/Aws.h>
#include <aws/dynamodb/DynamoDBClient.h>
#include <aws/dynamodb/model/PutItemRequest.h>
#include <aws/dynamodb/model/GetItemRequest.h>
#include <aws/dynamodb/model/AttributeValue.h>
#include "MovieRepository.h"

/**
 * Example demonstrating how to add a movie to DynamoDB using the MovieRepository class
 * 
 * This example shows:
 * 1. Creating a MovieRepository instance
 * 2. Adding a new movie to the database
 * 3. Verifying the movie was added by retrieving it
 */
int main()
{
    // Initialize the AWS SDK
    Aws::SDKOptions options;
    Aws::InitAPI(options);
    
    {
        // Create a MovieRepository instance
        MovieRepository movies;
        
        // Add "District 9" to the database
        // This demonstrates how to insert a new item into DynamoDB
        bool success = movies.Insert(
            "District 9",    // title
            2009,       // year
            "An extraterrestrial race forced to live in slum-like conditions on Earth suddenly finds a kindred spirit in a government agent who is exposed to their biotechnology.",     // plot
            8      // rating
        );
        
        if (success) {
            std::cout << "Movie added successfully" << std::endl;
            
            // Confirm that the movie was added by retrieving it
            auto movie = movies.Select(
                "District 9",    // title
                2009        // year
            );
            
            if (movie.has_value()) {
                // The movie was found
                std::cout << "Movie found: " << movie->ToString() << std::endl;
            } else {
                // The movie was not found
                std::cout << "Movie not found" << std::endl;
            }
        } else {
            std::cout << "Failed to add movie" << std::endl;
        }
    }
    
    // Shutdown the AWS SDK
    Aws::ShutdownAPI(options);
    return 0;
}
