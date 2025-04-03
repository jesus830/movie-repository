import boto3
import csv
import os

# This Python script generates Java code examples for the movie database application
# It creates sample files demonstrating CRUD operations with DynamoDB in Java

s3 = boto3.resource('s3')

def add_movie(id, title, year, plot, rating):
    """
    Generate Java code example for adding a movie to DynamoDB
    """
    file = f'''package com.example.moviedatabase;

import com.amazonaws.services.dynamodbv2.AmazonDynamoDB;
import com.amazonaws.services.dynamodbv2.AmazonDynamoDBClientBuilder;
import com.amazonaws.services.dynamodbv2.document.DynamoDB;
import com.amazonaws.services.dynamodbv2.document.Item;
import com.amazonaws.services.dynamodbv2.document.Table;
import com.amazonaws.services.dynamodbv2.document.spec.GetItemSpec;

/**
 * Example demonstrating how to add a movie to DynamoDB using the MovieRepository class
 * 
 * This example shows:
 * 1. Creating a MovieRepository instance
 * 2. Adding a new movie to the database
 * 3. Verifying the movie was added by retrieving it
 */
public class AddMovie {{

    public static void main(String[] args) {{
        // Create a MovieRepository instance
        MovieRepository movies = new MovieRepository();
        
        try {{
            // Add "{title}" to the database
            // This demonstrates how to insert a new item into DynamoDB
            boolean success = movies.insert(
                "{title}",    // title
                {year},       // year
                "{plot}",     // plot
                {rating}      // rating
            );
            
            if (success) {{
                System.out.println("Movie added successfully");
                
                // Confirm that the movie was added by retrieving it
                Movie movie = movies.select(
                    "{title}",    // title
                    {year}        // year
                );
                
                if (movie != null) {{
                    // The movie was found
                    System.out.println("Movie found: " + movie.toString());
                }} else {{
                    // The movie was not found
                    System.out.println("Movie not found");
                }}
            }} else {{
                System.out.println("Failed to add movie");
            }}
        }} catch (Exception e) {{
            System.err.println("Error adding movie: " + e.getMessage());
            e.printStackTrace();
        }}
    }}
}}
'''

    # Create local directory if it doesn't exist
    os.makedirs(f'java/examples/{year}', exist_ok=True)
    
    # Save the file locally
    with open(f'java/examples/{year}/{id}-add.java', 'w') as f:
        f.write(file)
    
    # Optionally upload to S3
    try:
        object = s3.Object('amazon-q-developer-customization-demo', f'imdb-demo/java/{year}/{id}-add.java')
        object.put(Body=file.encode('utf-8'))
    except Exception as e:
        print(f"S3 upload failed: {e}")


def delete_movie(id, title, year, plot, rating):
    """
    Generate Java code example for deleting a movie from DynamoDB
    """
    file = f'''package com.example.moviedatabase;

import com.amazonaws.services.dynamodbv2.AmazonDynamoDB;
import com.amazonaws.services.dynamodbv2.AmazonDynamoDBClientBuilder;
import com.amazonaws.services.dynamodbv2.document.DynamoDB;
import com.amazonaws.services.dynamodbv2.document.Table;

/**
 * Example demonstrating how to delete a movie from DynamoDB using the MovieRepository class
 * 
 * This example shows:
 * 1. Creating a MovieRepository instance
 * 2. Checking if a movie exists
 * 3. Deleting the movie if it exists
 */
public class DeleteMovie {{

    public static void main(String[] args) {{
        // Create a MovieRepository instance
        MovieRepository movies = new MovieRepository();
        
        try {{
            // Confirm that the movie exists in the database
            Movie movie = movies.select(
                "{title}",    // title
                {year}        // year
            );
            
            if (movie != null) {{
                // Delete the movie
                // This demonstrates how to remove an item from DynamoDB
                System.out.println("Deleting movie");
                boolean success = movies.delete(
                    "{title}",    // title
                    {year}        // year
                );
                
                if (success) {{
                    System.out.println("Movie deleted successfully");
                }} else {{
                    System.out.println("Failed to delete movie");
                }}
            }} else {{
                // Warn that the movie doesn't exist
                System.out.println("Movie not found; therefore, no need to delete it.");
            }}
        }} catch (Exception e) {{
            System.err.println("Error deleting movie: " + e.getMessage());
            e.printStackTrace();
        }}
    }}
}}
'''

    # Create local directory if it doesn't exist
    os.makedirs(f'java/examples/{year}', exist_ok=True)
    
    # Save the file locally
    with open(f'java/examples/{year}/{id}-delete.java', 'w') as f:
        f.write(file)
    
    # Optionally upload to S3
    try:
        object = s3.Object('amazon-q-developer-customization-demo', f'imdb-demo/java/{year}/{id}-delete.java')
        object.put(Body=file.encode('utf-8'))
    except Exception as e:
        print(f"S3 upload failed: {e}")


def get_movie(id, title, year, plot, rating):
    """
    Generate Java code example for retrieving a movie from DynamoDB
    """
    file = f'''package com.example.moviedatabase;

import com.amazonaws.services.dynamodbv2.AmazonDynamoDB;
import com.amazonaws.services.dynamodbv2.AmazonDynamoDBClientBuilder;
import com.amazonaws.services.dynamodbv2.document.DynamoDB;
import com.amazonaws.services.dynamodbv2.document.Item;
import com.amazonaws.services.dynamodbv2.document.Table;
import com.amazonaws.services.dynamodbv2.document.spec.GetItemSpec;

/**
 * Example demonstrating how to retrieve a movie from DynamoDB using the MovieRepository class
 * 
 * This example shows:
 * 1. Creating a MovieRepository instance
 * 2. Retrieving a movie by its primary key (title and year)
 * 3. Handling the case when a movie is found or not found
 */
public class GetMovie {{

    public static void main(String[] args) {{
        // Create a MovieRepository instance
        MovieRepository movies = new MovieRepository();
        
        try {{
            // Retrieve the movie from DynamoDB
            // This demonstrates how to get an item by its primary key
            Movie movie = movies.select(
                "{title}",    // title
                {year}        // year
            );
            
            if (movie != null) {{
                // The movie was found
                System.out.println("Movie found:");
                System.out.println("Title: " + movie.getTitle());
                System.out.println("Year: " + movie.getYear());
                System.out.println("Plot: " + movie.getPlot());
                System.out.println("Rating: " + movie.getRating());
            }} else {{
                // The movie was not found
                System.out.println("Movie not found");
            }}
        }} catch (Exception e) {{
            System.err.println("Error retrieving movie: " + e.getMessage());
            e.printStackTrace();
        }}
    }}
}}
'''

    # Create local directory if it doesn't exist
    os.makedirs(f'java/examples/{year}', exist_ok=True)
    
    # Save the file locally
    with open(f'java/examples/{year}/{id}-get.java', 'w') as f:
        f.write(file)
    
    # Optionally upload to S3
    try:
        object = s3.Object('amazon-q-developer-customization-demo', f'imdb-demo/java/{year}/{id}-get.java')
        object.put(Body=file.encode('utf-8'))
    except Exception as e:
        print(f"S3 upload failed: {e}")


def update_movie(id, title, year, plot, rating):
    """
    Generate Java code example for updating a movie in DynamoDB
    """
    file = f'''package com.example.moviedatabase;

import com.amazonaws.services.dynamodbv2.AmazonDynamoDB;
import com.amazonaws.services.dynamodbv2.AmazonDynamoDBClientBuilder;
import com.amazonaws.services.dynamodbv2.document.DynamoDB;
import com.amazonaws.services.dynamodbv2.document.Table;
import com.amazonaws.services.dynamodbv2.document.UpdateItemOutcome;
import com.amazonaws.services.dynamodbv2.document.spec.UpdateItemSpec;
import com.amazonaws.services.dynamodbv2.document.utils.ValueMap;
import com.amazonaws.services.dynamodbv2.model.ReturnValue;

/**
 * Example demonstrating how to update a movie in DynamoDB using the MovieRepository class
 * 
 * This example shows:
 * 1. Creating a MovieRepository instance
 * 2. Checking if a movie exists
 * 3. Updating the movie's attributes if it exists
 */
public class UpdateMovie {{

    public static void main(String[] args) {{
        // Create a MovieRepository instance
        MovieRepository movies = new MovieRepository();
        
        try {{
            // Check if the movie exists
            Movie movie = movies.select(
                "{title}",    // title
                {year}        // year
            );
            
            if (movie != null) {{
                // The movie was found, so update it
                // This demonstrates how to update an existing item in DynamoDB
                boolean success = movies.update(
                    "{title}",    // title
                    {year},       // year
                    "{plot}",     // plot
                    {rating}      // rating
                );
                
                if (success) {{
                    System.out.println("Movie updated successfully");
                }} else {{
                    System.out.println("Failed to update movie");
                }}
            }} else {{
                // The movie was not found, so we cannot update
                System.out.println("Movie not found");
            }}
        }} catch (Exception e) {{
            System.err.println("Error updating movie: " + e.getMessage());
            e.printStackTrace();
        }}
    }}
}}
'''

    # Create local directory if it doesn't exist
    os.makedirs(f'java/examples/{year}', exist_ok=True)
    
    # Save the file locally
    with open(f'java/examples/{year}/{id}-update.java', 'w') as f:
        f.write(file)
    
    # Optionally upload to S3
    try:
        object = s3.Object('amazon-q-developer-customization-demo', f'imdb-demo/java/{year}/{id}-update.java')
        object.put(Body=file.encode('utf-8'))
    except Exception as e:
        print(f"S3 upload failed: {e}")


def query_movies_by_year(year):
    """
    Generate Java code example for querying movies by year
    """
    file = f'''package com.example.moviedatabase;

import com.amazonaws.services.dynamodbv2.AmazonDynamoDB;
import com.amazonaws.services.dynamodbv2.AmazonDynamoDBClientBuilder;
import com.amazonaws.services.dynamodbv2.document.DynamoDB;
import com.amazonaws.services.dynamodbv2.document.Item;
import com.amazonaws.services.dynamodbv2.document.ItemCollection;
import com.amazonaws.services.dynamodbv2.document.QueryOutcome;
import com.amazonaws.services.dynamodbv2.document.Table;
import com.amazonaws.services.dynamodbv2.document.spec.QuerySpec;
import com.amazonaws.services.dynamodbv2.document.utils.ValueMap;
import java.util.Iterator;
import java.util.List;

/**
 * Example demonstrating how to query movies by year from DynamoDB using the MovieRepository class
 * 
 * This example shows:
 * 1. Creating a MovieRepository instance
 * 2. Querying for all movies from a specific year
 * 3. Processing the query results
 */
public class QueryMoviesByYear {{

    public static void main(String[] args) {{
        // Create a MovieRepository instance
        MovieRepository movies = new MovieRepository();
        
        try {{
            // Query movies from {year}
            // This demonstrates how to query items using a secondary index
            List<Movie> results = movies.queryByYear({year});
            
            System.out.println("Movies from {year}:");
            for (Movie movie : results) {{
                System.out.println("- " + movie.getTitle() + " (Rating: " + movie.getRating() + ")");
            }}
            
            System.out.println("Total movies found: " + results.size());
        }} catch (Exception e) {{
            System.err.println("Error querying movies: " + e.getMessage());
            e.printStackTrace();
        }}
    }}
}}
'''

    # Create local directory if it doesn't exist
    os.makedirs(f'java/examples/{year}', exist_ok=True)
    
    # Save the file locally
    with open(f'java/examples/{year}/query-by-year.java', 'w') as f:
        f.write(file)
    
    # Optionally upload to S3
    try:
        object = s3.Object('amazon-q-developer-customization-demo', f'imdb-demo/java/{year}/query-by-year.java')
        object.put(Body=file.encode('utf-8'))
    except Exception as e:
        print(f"S3 upload failed: {e}")


def main():
    """
    Main function to process the movies CSV and generate code examples
    """
    # Create examples directory if it doesn't exist
    os.makedirs('java/examples', exist_ok=True)
    
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
        print(f"Generated Java examples for {movie['title']} ({movie['year']})")
    
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
                    
                    print(f"Generated Java examples for {title} ({year})")
                    count += 1
        except Exception as e:
            print(f"Error processing CSV: {e}")


if __name__ == "__main__":
    main()
