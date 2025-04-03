#include <iostream>
#include <aws/core/Aws.h>
#include <aws/dynamodb/DynamoDBClient.h>
#include <aws/dynamodb/model/GetItemRequest.h>
#include <aws/dynamodb/model/AttributeValue.h>
#include "MovieRepository.h"

/**
 * Example demonstrating how to retrieve a movie from DynamoDB using the MovieRepository class
 * 
 * This example shows:
 * 1. Creating a MovieRepository instance
 * 2. Retrieving a movie by its primary key (title and year)
 * 3. Handling the case when a movie is found or not found
 */
int main()
{
    // Initialize the AWS SDK
    Aws::SDKOptions options;
    Aws::InitAPI(options);
    
    {
        // Create a MovieRepository instance
        MovieRepository movies;
        
        // Retrieve the movie from DynamoDB
        // This demonstrates how to get an item by its primary key
        auto movie = movies.Select(
            "What We Do in the Shadows",    // title
            2014        // year
        );
        
        if (movie.has_value()) {
            // The movie was found
            std::cout << "Movie found:" << std::endl;
            std::cout << "Title: " << movie->GetTitle() << std::endl;
            std::cout << "Year: " << movie->GetYear() << std::endl;
            std::cout << "Plot: " << movie->GetPlot() << std::endl;
            std::cout << "Rating: " << movie->GetRating() << std::endl;
        } else {
            // The movie was not found
            std::cout << "Movie not found" << std::endl;
        }
    }
    
    // Shutdown the AWS SDK
    Aws::ShutdownAPI(options);
    return 0;
}
