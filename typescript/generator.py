import boto3
import csv
import os

# This Python script generates TypeScript code examples for the movie database application
# It creates sample files demonstrating CRUD operations with DynamoDB in TypeScript

s3 = boto3.resource('s3')

def add_movie(id, title, year, plot, rating):
    """
    Generate TypeScript code example for adding a movie to DynamoDB
    """
    file = f'''import * as AWS from 'aws-sdk';
import {{ MovieRepository }} from './MovieRepository';
import {{ Movie }} from './Movie';

/**
 * Example demonstrating how to add a movie to DynamoDB using the MovieRepository class
 * 
 * This example shows:
 * 1. Creating a MovieRepository instance
 * 2. Adding a new movie to the database
 * 3. Verifying the movie was added by retrieving it
 */
async function addMovie(): Promise<void> {{
    // Configure AWS SDK (assuming credentials are set via environment variables or AWS config)
    AWS.config.update({{ region: 'us-west-2' }});
    
    // Create a MovieRepository instance
    const movies = new MovieRepository();
    
    try {{
        // Add "{title}" to the database
        // This demonstrates how to insert a new item into DynamoDB
        const success = await movies.insert({{
            title: "{title}",
            year: {year},
            plot: "{plot}",
            rating: {rating}
        }});
        
        if (success) {{
            console.log('Movie added successfully');
            
            // Confirm that the movie was added by retrieving it
            const movie = await movies.select({{
                title: "{title}",
                year: {year}
            }});
            
            if (movie) {{
                // The movie was found
                console.log('Movie found:', movie);
            }} else {{
                // The movie was not found
                console.log('Movie not found');
            }}
        }} else {{
            console.log('Failed to add movie');
        }}
    }} catch (error) {{
        console.error('Error adding movie:', error);
    }}
}}

// Execute the function
addMovie().catch(err => console.error('Execution error:', err));
'''

    # Create local directory if it doesn't exist
    os.makedirs(f'typescript/examples/{year}', exist_ok=True)
    
    # Save the file locally
    with open(f'typescript/examples/{year}/{id}-add.ts', 'w') as f:
        f.write(file)
    
    # Optionally upload to S3
    try:
        object = s3.Object('amazon-q-developer-customization-demo', f'imdb-demo/typescript/{year}/{id}-add.ts')
        object.put(Body=file.encode('utf-8'))
    except Exception as e:
        print(f"S3 upload failed: {e}")


def delete_movie(id, title, year, plot, rating):
    """
    Generate TypeScript code example for deleting a movie from DynamoDB
    """
    file = f'''import * as AWS from 'aws-sdk';
import {{ MovieRepository }} from './MovieRepository';
import {{ Movie }} from './Movie';

/**
 * Example demonstrating how to delete a movie from DynamoDB using the MovieRepository class
 * 
 * This example shows:
 * 1. Creating a MovieRepository instance
 * 2. Checking if a movie exists
 * 3. Deleting the movie if it exists
 */
async function deleteMovie(): Promise<void> {{
    // Configure AWS SDK (assuming credentials are set via environment variables or AWS config)
    AWS.config.update({{ region: 'us-west-2' }});
    
    // Create a MovieRepository instance
    const movies = new MovieRepository();
    
    try {{
        // Confirm that the movie exists in the database
        const movie = await movies.select({{
            title: "{title}",
            year: {year}
        }});
        
        if (movie) {{
            // Delete the movie
            // This demonstrates how to remove an item from DynamoDB
            console.log('Deleting movie');
            const success = await movies.delete({{
                title: "{title}",
                year: {year}
            }});
            
            if (success) {{
                console.log('Movie deleted successfully');
            }} else {{
                console.log('Failed to delete movie');
            }}
        }} else {{
            // Warn that the movie doesn't exist
            console.log('Movie not found; therefore, no need to delete it.');
        }}
    }} catch (error) {{
        console.error('Error deleting movie:', error);
    }}
}}

// Execute the function
deleteMovie().catch(err => console.error('Execution error:', err));
'''

    # Create local directory if it doesn't exist
    os.makedirs(f'typescript/examples/{year}', exist_ok=True)
    
    # Save the file locally
    with open(f'typescript/examples/{year}/{id}-delete.ts', 'w') as f:
        f.write(file)
    
    # Optionally upload to S3
    try:
        object = s3.Object('amazon-q-developer-customization-demo', f'imdb-demo/typescript/{year}/{id}-delete.ts')
        object.put(Body=file.encode('utf-8'))
    except Exception as e:
        print(f"S3 upload failed: {e}")


def get_movie(id, title, year, plot, rating):
    """
    Generate TypeScript code example for retrieving a movie from DynamoDB
    """
    file = f'''import * as AWS from 'aws-sdk';
import {{ MovieRepository }} from './MovieRepository';
import {{ Movie }} from './Movie';

/**
 * Example demonstrating how to retrieve a movie from DynamoDB using the MovieRepository class
 * 
 * This example shows:
 * 1. Creating a MovieRepository instance
 * 2. Retrieving a movie by its primary key (title and year)
 * 3. Handling the case when a movie is found or not found
 */
async function getMovie(): Promise<void> {{
    // Configure AWS SDK (assuming credentials are set via environment variables or AWS config)
    AWS.config.update({{ region: 'us-west-2' }});
    
    // Create a MovieRepository instance
    const movies = new MovieRepository();
    
    try {{
        // Retrieve the movie from DynamoDB
        // This demonstrates how to get an item by its primary key
        const movie = await movies.select({{
            title: "{title}",
            year: {year}
        }});
        
        if (movie) {{
            // The movie was found
            console.log('Movie found:');
            console.log('Title:', movie.title);
            console.log('Year:', movie.year);
            console.log('Plot:', movie.plot);
            console.log('Rating:', movie.rating);
        }} else {{
            // The movie was not found
            console.log('Movie not found');
        }}
    }} catch (error) {{
        console.error('Error retrieving movie:', error);
    }}
}}

// Execute the function
getMovie().catch(err => console.error('Execution error:', err));
'''

    # Create local directory if it doesn't exist
    os.makedirs(f'typescript/examples/{year}', exist_ok=True)
    
    # Save the file locally
    with open(f'typescript/examples/{year}/{id}-get.ts', 'w') as f:
        f.write(file)
    
    # Optionally upload to S3
    try:
        object = s3.Object('amazon-q-developer-customization-demo', f'imdb-demo/typescript/{year}/{id}-get.ts')
        object.put(Body=file.encode('utf-8'))
    except Exception as e:
        print(f"S3 upload failed: {e}")


def update_movie(id, title, year, plot, rating):
    """
    Generate TypeScript code example for updating a movie in DynamoDB
    """
    file = f'''import * as AWS from 'aws-sdk';
import {{ MovieRepository }} from './MovieRepository';
import {{ Movie }} from './Movie';

/**
 * Example demonstrating how to update a movie in DynamoDB using the MovieRepository class
 * 
 * This example shows:
 * 1. Creating a MovieRepository instance
 * 2. Checking if a movie exists
 * 3. Updating the movie's attributes if it exists
 */
async function updateMovie(): Promise<void> {{
    // Configure AWS SDK (assuming credentials are set via environment variables or AWS config)
    AWS.config.update({{ region: 'us-west-2' }});
    
    // Create a MovieRepository instance
    const movies = new MovieRepository();
    
    try {{
        // Check if the movie exists
        const movie = await movies.select({{
            title: "{title}",
            year: {year}
        }});
        
        if (movie) {{
            // The movie was found, so update it
            // This demonstrates how to update an existing item in DynamoDB
            const success = await movies.update({{
                title: "{title}",
                year: {year},
                plot: "{plot}",
                rating: {rating}
            }});
            
            if (success) {{
                console.log('Movie updated successfully');
            }} else {{
                console.log('Failed to update movie');
            }}
        }} else {{
            // The movie was not found, so we cannot update
            console.log('Movie not found');
        }}
    }} catch (error) {{
        console.error('Error updating movie:', error);
    }}
}}

// Execute the function
updateMovie().catch(err => console.error('Execution error:', err));
'''

    # Create local directory if it doesn't exist
    os.makedirs(f'typescript/examples/{year}', exist_ok=True)
    
    # Save the file locally
    with open(f'typescript/examples/{year}/{id}-update.ts', 'w') as f:
        f.write(file)
    
    # Optionally upload to S3
    try:
        object = s3.Object('amazon-q-developer-customization-demo', f'imdb-demo/typescript/{year}/{id}-update.ts')
        object.put(Body=file.encode('utf-8'))
    except Exception as e:
        print(f"S3 upload failed: {e}")


def query_movies_by_year(year):
    """
    Generate TypeScript code example for querying movies by year
    """
    file = f'''import * as AWS from 'aws-sdk';
import {{ MovieRepository }} from './MovieRepository';
import {{ Movie }} from './Movie';

/**
 * Example demonstrating how to query movies by year from DynamoDB using the MovieRepository class
 * 
 * This example shows:
 * 1. Creating a MovieRepository instance
 * 2. Querying for all movies from a specific year
 * 3. Processing the query results
 */
async function queryMoviesByYear(): Promise<void> {{
    // Configure AWS SDK (assuming credentials are set via environment variables or AWS config)
    AWS.config.update({{ region: 'us-west-2' }});
    
    // Create a MovieRepository instance
    const movies = new MovieRepository();
    
    try {{
        // Query movies from {year}
        // This demonstrates how to query items using a secondary index
        const results: Movie[] = await movies.queryByYear({year});
        
        console.log(`Movies from {year}:`);
        results.forEach(movie => {{
            console.log(`- ${{movie.title}} (Rating: ${{movie.rating}})`);
        }});
        
        console.log(`Total movies found: ${{results.length}}`);
    }} catch (error) {{
        console.error('Error querying movies:', error);
    }}
}}

// Execute the function
queryMoviesByYear().catch(err => console.error('Execution error:', err));
'''

    # Create local directory if it doesn't exist
    os.makedirs(f'typescript/examples/{year}', exist_ok=True)
    
    # Save the file locally
    with open(f'typescript/examples/{year}/query-by-year.ts', 'w') as f:
        f.write(file)
    
    # Optionally upload to S3
    try:
        object = s3.Object('amazon-q-developer-customization-demo', f'imdb-demo/typescript/{year}/query-by-year.ts')
        object.put(Body=file.encode('utf-8'))
    except Exception as e:
        print(f"S3 upload failed: {e}")


def create_movie_interface():
    """
    Generate TypeScript interface for Movie
    """
    file = '''/**
 * Interface representing a Movie in the database
 */
export interface Movie {
    /**
     * The title of the movie (primary key)
     */
    title: string;
    
    /**
     * The release year of the movie (sort key)
     */
    year: number;
    
    /**
     * A brief summary of the movie's plot
     */
    plot?: string;
    
    /**
     * The movie's rating on a scale of 1-10
     */
    rating?: number;
    
    /**
     * Optional list of actors in the movie
     */
    actors?: string[];
    
    /**
     * Optional director of the movie
     */
    director?: string;
}
'''

    # Create local directory if it doesn't exist
    os.makedirs('typescript/examples', exist_ok=True)
    
    # Save the file locally
    with open('typescript/examples/Movie.ts', 'w') as f:
        f.write(file)
    
    # Optionally upload to S3
    try:
        object = s3.Object('amazon-q-developer-customization-demo', 'imdb-demo/typescript/Movie.ts')
        object.put(Body=file.encode('utf-8'))
    except Exception as e:
        print(f"S3 upload failed: {e}")


def main():
    """
    Main function to process the movies CSV and generate code examples
    """
    # Create examples directory if it doesn't exist
    os.makedirs('typescript/examples', exist_ok=True)
    
    # Create the Movie interface
    create_movie_interface()
    
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
        print(f"Generated TypeScript examples for {movie['title']} ({movie['year']})")
    
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
                    
                    print(f"Generated TypeScript examples for {title} ({year})")
                    count += 1
        except Exception as e:
            print(f"Error processing CSV: {e}")


if __name__ == "__main__":
    main()
