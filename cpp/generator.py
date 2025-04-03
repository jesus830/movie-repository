import boto3
import csv
import os

# This Python script generates C++ code examples for the movie database application
# It creates sample files demonstrating CRUD operations with DynamoDB in C++

s3 = boto3.resource('s3')

def add_movie(id, title, year, plot, rating):
    """
    Generate C++ code example for adding a movie to DynamoDB
    """
    file = f'''#include <iostream>
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
{{
    // Initialize the AWS SDK
    Aws::SDKOptions options;
    Aws::InitAPI(options);
    
    {{
        // Create a MovieRepository instance
        MovieRepository movies;
        
        // Add "{title}" to the database
        // This demonstrates how to insert a new item into DynamoDB
        bool success = movies.Insert(
            "{title}",    // title
            {year},       // year
            "{plot}",     // plot
            {rating}      // rating
        );
        
        if (success) {{
            std::cout << "Movie added successfully" << std::endl;
            
            // Confirm that the movie was added by retrieving it
            auto movie = movies.Select(
                "{title}",    // title
                {year}        // year
            );
            
            if (movie.has_value()) {{
                // The movie was found
                std::cout << "Movie found: " << movie->ToString() << std::endl;
            }} else {{
                // The movie was not found
                std::cout << "Movie not found" << std::endl;
            }}
        }} else {{
            std::cout << "Failed to add movie" << std::endl;
        }}
    }}
    
    // Shutdown the AWS SDK
    Aws::ShutdownAPI(options);
    return 0;
}}
'''

    # Create local directory if it doesn't exist
    os.makedirs(f'cpp/examples/{year}', exist_ok=True)
    
    # Save the file locally
    with open(f'cpp/examples/{year}/{id}-add.cpp', 'w') as f:
        f.write(file)
    
    # Optionally upload to S3
    try:
        object = s3.Object('amazon-q-developer-customization-demo', f'imdb-demo/cpp/{year}/{id}-add.cpp')
        object.put(Body=file.encode('utf-8'))
    except Exception as e:
        print(f"S3 upload failed: {e}")


def delete_movie(id, title, year, plot, rating):
    """
    Generate C++ code example for deleting a movie from DynamoDB
    """
    file = f'''#include <iostream>
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
{{
    // Initialize the AWS SDK
    Aws::SDKOptions options;
    Aws::InitAPI(options);
    
    {{
        // Create a MovieRepository instance
        MovieRepository movies;
        
        // Confirm that the movie exists in the database
        auto movie = movies.Select(
            "{title}",    // title
            {year}        // year
        );
        
        if (movie.has_value()) {{
            // Delete the movie
            // This demonstrates how to remove an item from DynamoDB
            std::cout << "Deleting movie" << std::endl;
            bool success = movies.Delete(
                "{title}",    // title
                {year}        // year
            );
            
            if (success) {{
                std::cout << "Movie deleted successfully" << std::endl;
            }} else {{
                std::cout << "Failed to delete movie" << std::endl;
            }}
        }} else {{
            // Warn that the movie doesn't exist
            std::cout << "Movie not found; therefore, no need to delete it." << std::endl;
        }}
    }}
    
    // Shutdown the AWS SDK
    Aws::ShutdownAPI(options);
    return 0;
}}
'''

    # Create local directory if it doesn't exist
    os.makedirs(f'cpp/examples/{year}', exist_ok=True)
    
    # Save the file locally
    with open(f'cpp/examples/{year}/{id}-delete.cpp', 'w') as f:
        f.write(file)
    
    # Optionally upload to S3
    try:
        object = s3.Object('amazon-q-developer-customization-demo', f'imdb-demo/cpp/{year}/{id}-delete.cpp')
        object.put(Body=file.encode('utf-8'))
    except Exception as e:
        print(f"S3 upload failed: {e}")


def get_movie(id, title, year, plot, rating):
    """
    Generate C++ code example for retrieving a movie from DynamoDB
    """
    file = f'''#include <iostream>
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
{{
    // Initialize the AWS SDK
    Aws::SDKOptions options;
    Aws::InitAPI(options);
    
    {{
        // Create a MovieRepository instance
        MovieRepository movies;
        
        // Retrieve the movie from DynamoDB
        // This demonstrates how to get an item by its primary key
        auto movie = movies.Select(
            "{title}",    // title
            {year}        // year
        );
        
        if (movie.has_value()) {{
            // The movie was found
            std::cout << "Movie found:" << std::endl;
            std::cout << "Title: " << movie->GetTitle() << std::endl;
            std::cout << "Year: " << movie->GetYear() << std::endl;
            std::cout << "Plot: " << movie->GetPlot() << std::endl;
            std::cout << "Rating: " << movie->GetRating() << std::endl;
        }} else {{
            // The movie was not found
            std::cout << "Movie not found" << std::endl;
        }}
    }}
    
    // Shutdown the AWS SDK
    Aws::ShutdownAPI(options);
    return 0;
}}
'''

    # Create local directory if it doesn't exist
    os.makedirs(f'cpp/examples/{year}', exist_ok=True)
    
    # Save the file locally
    with open(f'cpp/examples/{year}/{id}-get.cpp', 'w') as f:
        f.write(file)
    
    # Optionally upload to S3
    try:
        object = s3.Object('amazon-q-developer-customization-demo', f'imdb-demo/cpp/{year}/{id}-get.cpp')
        object.put(Body=file.encode('utf-8'))
    except Exception as e:
        print(f"S3 upload failed: {e}")


def update_movie(id, title, year, plot, rating):
    """
    Generate C++ code example for updating a movie in DynamoDB
    """
    file = f'''#include <iostream>
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
{{
    // Initialize the AWS SDK
    Aws::SDKOptions options;
    Aws::InitAPI(options);
    
    {{
        // Create a MovieRepository instance
        MovieRepository movies;
        
        // Check if the movie exists
        auto movie = movies.Select(
            "{title}",    // title
            {year}        // year
        );
        
        if (movie.has_value()) {{
            // The movie was found, so update it
            // This demonstrates how to update an existing item in DynamoDB
            bool success = movies.Update(
                "{title}",    // title
                {year},       // year
                "{plot}",     // plot
                {rating}      // rating
            );
            
            if (success) {{
                std::cout << "Movie updated successfully" << std::endl;
            }} else {{
                std::cout << "Failed to update movie" << std::endl;
            }}
        }} else {{
            // The movie was not found, so we cannot update
            std::cout << "Movie not found" << std::endl;
        }}
    }}
    
    // Shutdown the AWS SDK
    Aws::ShutdownAPI(options);
    return 0;
}}
'''

    # Create local directory if it doesn't exist
    os.makedirs(f'cpp/examples/{year}', exist_ok=True)
    
    # Save the file locally
    with open(f'cpp/examples/{year}/{id}-update.cpp', 'w') as f:
        f.write(file)
    
    # Optionally upload to S3
    try:
        object = s3.Object('amazon-q-developer-customization-demo', f'imdb-demo/cpp/{year}/{id}-update.cpp')
        object.put(Body=file.encode('utf-8'))
    except Exception as e:
        print(f"S3 upload failed: {e}")


def query_movies_by_year(year):
    """
    Generate C++ code example for querying movies by year
    """
    file = f'''#include <iostream>
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
{{
    // Initialize the AWS SDK
    Aws::SDKOptions options;
    Aws::InitAPI(options);
    
    {{
        // Create a MovieRepository instance
        MovieRepository movies;
        
        // Query movies from {year}
        // This demonstrates how to query items using a secondary index
        auto results = movies.QueryByYear({year});
        
        std::cout << "Movies from {year}:" << std::endl;
        for (const auto& movie : results) {{
            std::cout << "- " << movie.GetTitle() << " (Rating: " << movie.GetRating() << ")" << std::endl;
        }}
        
        std::cout << "Total movies found: " << results.size() << std::endl;
    }}
    
    // Shutdown the AWS SDK
    Aws::ShutdownAPI(options);
    return 0;
}}
'''

    # Create local directory if it doesn't exist
    os.makedirs(f'cpp/examples/{year}', exist_ok=True)
    
    # Save the file locally
    with open(f'cpp/examples/{year}/query-by-year.cpp', 'w') as f:
        f.write(file)
    
    # Optionally upload to S3
    try:
        object = s3.Object('amazon-q-developer-customization-demo', f'imdb-demo/cpp/{year}/query-by-year.cpp')
        object.put(Body=file.encode('utf-8'))
    except Exception as e:
        print(f"S3 upload failed: {e}")


def main():
    """
    Main function to process the movies CSV and generate code examples
    """
    # Create examples directory if it doesn't exist
    os.makedirs('cpp/examples', exist_ok=True)
    
    # Process a few sample movies to generate examples
    sample_movies = [
        {"id": "the-shawshank-redemption", "title": "The Shawshank Redemption", "year": 1994, "plot": "Two imprisoned men bond over a number of years.", "rating": 9.3},
        {"id": "the-godfather", "title": "The Godfather", "year": 1972, "plot": "The aging patriarch of an organized crime dynasty.", "rating": 9.2},
        {"id": "pulp-fiction", "title": "Pulp Fiction", "year": 1994, "plot": "The lives of two mob hitmen, a boxer, a gangster and his wife.", "rating": 8.9}
    ]
    
    for movie in sample_movies:
        add_movie(movie["id"], movie["title"], movie["year"], movie["plot"], movie["rating"])
        delete_movie(movie["id"], movie["title"], movie["year"], movie["plot"], movie["rating"])
        get_movie(movie["id"], movie["title"], movie["year"], movie["plot"], movie["rating"])
        update_movie(movie["id"], movie["title"], movie["year"], movie["plot"], movie["rating"])
        query_movies_by_year(movie["year"])
        print(f"Generated C++ examples for {movie['title']} ({movie['year']})")
    
    # Optionally process movies from CSV file if it exists
    csv_path = 'movies.csv'
    if os.path.exists(csv_path):
        try:
            with open(csv_path, 'r') as file:
                # Create a CSV reader object
                csv_reader = csv.reader(file)
                
                # Skip the header row
                next(csv_reader)
                
                # Process a limited number of rows to avoid generating too many files
                count = 0
                for row in csv_reader:
                        
                    title = row[1].replace("\"", "")
                    id = ''.join(letter for letter in title.lower().replace(' ','-') if letter.isalnum() or letter == '-')
                    plot = row[3].replace("\"", "'")
                    year = row[6]
                    rating = row[8] if row[8] else "7.0"  # Default rating if missing
                    
                    add_movie(id, title, year, plot, rating)
                    delete_movie(id, title, year, plot, rating)
                    get_movie(id, title, year, plot, rating)
                    update_movie(id, title, year, plot, rating)
                    
                    print(f"Generated C++ examples for {title} ({year})")
                    count += 1
        except Exception as e:
            print(f"Error processing CSV: {e}")


if __name__ == "__main__":
    main()
