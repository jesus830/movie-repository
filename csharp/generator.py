import boto3
import csv
import os

# This Python script generates C# code examples for the movie database application
# It creates sample files demonstrating CRUD operations with DynamoDB in C#

s3 = boto3.resource('s3')

def add_movie(id, title, year, plot, rating):
    """
    Generate C# code example for adding a movie to DynamoDB
    """
    file = f'''using System;
using System.Threading.Tasks;
using Amazon.DynamoDBv2;
using Amazon.DynamoDBv2.Model;
using System.Collections.Generic;

namespace MovieDatabase
{{
    class Program
    {{
        static async Task Main(string[] args)
        {{
            // Create a MovieRepository instance
            var movies = new MovieRepository();

            // Add "{title}" to the database
            // This demonstrates how to insert a new item into DynamoDB
            await movies.InsertAsync(
                title: "{title}",
                year: {year},
                plot: "{plot}",
                rating: {rating}
            );

            // Confirm that the movie was added by retrieving it
            var movie = await movies.SelectAsync(
                title: "{title}",
                year: {year}
            );

            if (movie != null)
            {{
                // The movie was found
                Console.WriteLine($"Movie found: {{movie}}");
            }}
            else
            {{
                // The movie was not found
                Console.WriteLine("Movie not found");
            }}
        }}
    }}
}}
'''

    # Create local directory if it doesn't exist
    os.makedirs(f'csharp/examples/{year}', exist_ok=True)
    
    # Save the file locally
    with open(f'csharp/examples/{year}/{id}-add.cs', 'w') as f:
        f.write(file)
    
    # Optionally upload to S3
    try:
        object = s3.Object('amazon-q-developer-customization-demo', f'imdb-demo/csharp/{year}/{id}-add.cs')
        object.put(Body=file.encode('utf-8'))
    except Exception as e:
        print(f"S3 upload failed: {e}")


def delete_movie(id, title, year, plot, rating):
    """
    Generate C# code example for deleting a movie from DynamoDB
    """
    file = f'''using System;
using System.Threading.Tasks;
using Amazon.DynamoDBv2;
using Amazon.DynamoDBv2.Model;
using System.Collections.Generic;

namespace MovieDatabase
{{
    class Program
    {{
        static async Task Main(string[] args)
        {{
            // Create a MovieRepository instance
            var movies = new MovieRepository();

            // Confirm that the movie exists in the database
            var movie = await movies.SelectAsync(
                title: "{title}",
                year: {year}
            );

            if (movie != null)
            {{
                // Delete the movie
                // This demonstrates how to remove an item from DynamoDB
                Console.WriteLine("Deleting movie");
                await movies.DeleteAsync(
                    title: "{title}",
                    year: {year}
                );
            }}
            else
            {{
                // Warn that the movie doesn't exist
                Console.WriteLine("Movie not found; therefore, no need to delete it.");
            }}
        }}
    }}
}}
'''

    # Create local directory if it doesn't exist
    os.makedirs(f'csharp/examples/{year}', exist_ok=True)
    
    # Save the file locally
    with open(f'csharp/examples/{year}/{id}-delete.cs', 'w') as f:
        f.write(file)
    
    # Optionally upload to S3
    try:
        object = s3.Object('amazon-q-developer-customization-demo', f'imdb-demo/csharp/{year}/{id}-delete.cs')
        object.put(Body=file.encode('utf-8'))
    except Exception as e:
        print(f"S3 upload failed: {e}")


def get_movie(id, title, year, plot, rating):
    """
    Generate C# code example for retrieving a movie from DynamoDB
    """
    file = f'''using System;
using System.Threading.Tasks;
using Amazon.DynamoDBv2;
using Amazon.DynamoDBv2.Model;
using System.Collections.Generic;

namespace MovieDatabase
{{
    class Program
    {{
        static async Task Main(string[] args)
        {{
            // Create a MovieRepository instance
            var movies = new MovieRepository();

            // Retrieve the movie from DynamoDB
            // This demonstrates how to get an item by its primary key
            var movie = await movies.SelectAsync(
                title: "{title}",
                year: {year}
            );

            if (movie != null)
            {{
                // The movie was found
                Console.WriteLine("Movie found:");
                Console.WriteLine($"Title: {{movie["title"]}}");
                Console.WriteLine($"Year: {{movie["year"]}}");
                Console.WriteLine($"Plot: {{movie["plot"]}}");
                Console.WriteLine($"Rating: {{movie["rating"]}}");
            }}
            else
            {{
                // The movie was not found
                Console.WriteLine("Movie not found");
            }}
        }}
    }}
}}
'''

    # Create local directory if it doesn't exist
    os.makedirs(f'csharp/examples/{year}', exist_ok=True)
    
    # Save the file locally
    with open(f'csharp/examples/{year}/{id}-get.cs', 'w') as f:
        f.write(file)
    
    # Optionally upload to S3
    try:
        object = s3.Object('amazon-q-developer-customization-demo', f'imdb-demo/csharp/{year}/{id}-get.cs')
        object.put(Body=file.encode('utf-8'))
    except Exception as e:
        print(f"S3 upload failed: {e}")


def update_movie(id, title, year, plot, rating):
    """
    Generate C# code example for updating a movie in DynamoDB
    """
    file = f'''using System;
using System.Threading.Tasks;
using Amazon.DynamoDBv2;
using Amazon.DynamoDBv2.Model;
using System.Collections.Generic;

namespace MovieDatabase
{{
    class Program
    {{
        static async Task Main(string[] args)
        {{
            // Create a MovieRepository instance
            var movies = new MovieRepository();

            // Check if the movie exists
            var movie = await movies.SelectAsync(
                title: "{title}",
                year: {year}
            );

            if (movie != null)
            {{
                // The movie was found, so update it
                // This demonstrates how to update an existing item in DynamoDB
                await movies.UpdateAsync(
                    title: "{title}",
                    year: {year},
                    plot: "{plot}",
                    rating: {rating}
                );
                Console.WriteLine("Movie updated");
            }}
            else
            {{
                // The movie was not found, so we cannot update
                Console.WriteLine("Movie not found");
            }}
        }}
    }}
}}
'''

    # Create local directory if it doesn't exist
    os.makedirs(f'csharp/examples/{year}', exist_ok=True)
    
    # Save the file locally
    with open(f'csharp/examples/{year}/{id}-update.cs', 'w') as f:
        f.write(file)
    
    # Optionally upload to S3
    try:
        object = s3.Object('amazon-q-developer-customization-demo', f'imdb-demo/csharp/{year}/{id}-update.cs')
        object.put(Body=file.encode('utf-8'))
    except Exception as e:
        print(f"S3 upload failed: {e}")


def query_movies_by_year(year):
    """
    Generate C# code example for querying movies by year
    """
    file = f'''using System;
using System.Threading.Tasks;
using Amazon.DynamoDBv2;
using Amazon.DynamoDBv2.Model;
using System.Collections.Generic;

namespace MovieDatabase
{{
    class Program
    {{
        static async Task Main(string[] args)
        {{
            // Create a MovieRepository instance
            var movies = new MovieRepository();

            // Query movies from {year}
            // This demonstrates how to query items using a secondary index
            var results = await movies.QueryByYearAsync({year});

            Console.WriteLine($"Movies from {year}:");
            foreach (var movie in results)
            {{
                Console.WriteLine($"- {{movie["title"]}} (Rating: {{movie["rating"]}})");
            }}
        }}
    }}
}}
'''

    # Create local directory if it doesn't exist
    os.makedirs(f'csharp/examples/{year}', exist_ok=True)
    
    # Save the file locally
    with open(f'csharp/examples/{year}/query-by-year.cs', 'w') as f:
        f.write(file)
    
    # Optionally upload to S3
    try:
        object = s3.Object('amazon-q-developer-customization-demo', f'imdb-demo/csharp/{year}/query-by-year.cs')
        object.put(Body=file.encode('utf-8'))
    except Exception as e:
        print(f"S3 upload failed: {e}")


def main():
    """
    Main function to process the movies CSV and generate code examples
    """
    # Create examples directory if it doesn't exist
    os.makedirs('csharp/examples', exist_ok=True)
    
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
        print(f"Generated C# examples for {movie['title']} ({movie['year']})")
    
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
                    
                    print(f"Generated C# examples for {title} ({year})")
                    count += 1
        except Exception as e:
            print(f"Error processing CSV: {e}")


if __name__ == "__main__":
    main()
