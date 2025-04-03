#include <iostream>
#include <aws/core/Aws.h>
#include <aws/dynamodb/DynamoDBClient.h>
#include <aws/dynamodb/model/QueryRequest.h>
#include <aws/dynamodb/model/AttributeValue.h>
#include "MovieRepository.h"

/**
 * Example demonstrating how to query movies by year from DynamoDB using the MovieRepository class
 * 
 * This example shows:
 * 1. Creating a MovieRepository instance
 * 2. Querying for all movies from a specific year
 * 3. Processing the query results
 */
int main()
{
    // Initialize the AWS SDK
    Aws::SDKOptions options;
    Aws::InitAPI(options);
    
    {
        // Create a MovieRepository instance
        MovieRepository movies;
        
        // Query movies from 1994
        // This demonstrates how to query items using a secondary index
        auto results = movies.QueryByYear(1994);
        
        std::cout << "Movies from 1994:" << std::endl;
        for (const auto& movie : results) {
            std::cout << "- " << movie.GetTitle() << " (Rating: " << movie.GetRating() << ")" << std::endl;
        }
        
        std::cout << "Total movies found: " << results.size() << std::endl;
    }
    
    // Shutdown the AWS SDK
    Aws::ShutdownAPI(options);
    return 0;
}
