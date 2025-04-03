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
        
        // Add "Twin Peaks: The Missing Pieces" to the database
        // This demonstrates how to insert a new item into DynamoDB
        bool success = movies.Insert(
            "Twin Peaks: The Missing Pieces",    // title
            2014,       // year
            "Twin Peaks before Twin Peaks (1990) and at the same time not always and entirely in the same place as Twin Peaks: Fire Walk with Me (1992). A feature film which presents deleted scenes from Twin Peaks: Fire Walk with Me (1992) assembled together for the first time in an untold portion of the story's prequel.",     // plot
            8.1      // rating
        );
        
        if (success) {
            std::cout << "Movie added successfully" << std::endl;
            
            // Confirm that the movie was added by retrieving it
            auto movie = movies.Select(
                "Twin Peaks: The Missing Pieces",    // title
                2014        // year
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
