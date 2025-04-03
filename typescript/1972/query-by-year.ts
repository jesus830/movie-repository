import * as AWS from 'aws-sdk';
import { MovieRepository } from './MovieRepository';
import { Movie } from './Movie';

/**
 * Example demonstrating how to query movies by year from DynamoDB using the MovieRepository class
 * 
 * This example shows:
 * 1. Creating a MovieRepository instance
 * 2. Querying for all movies from a specific year
 * 3. Processing the query results
 */
async function queryMoviesByYear(): Promise<void> {
    // Configure AWS SDK (assuming credentials are set via environment variables or AWS config)
    AWS.config.update({ region: 'us-west-2' });
    
    // Create a MovieRepository instance
    const movies = new MovieRepository();
    
    try {
        // Query movies from 1972
        // This demonstrates how to query items using a secondary index
        const results: Movie[] = await movies.queryByYear(1972);
        
        console.log(`Movies from 1972:`);
        results.forEach(movie => {
            console.log(`- ${movie.title} (Rating: ${movie.rating})`);
        });
        
        console.log(`Total movies found: ${results.length}`);
    } catch (error) {
        console.error('Error querying movies:', error);
    }
}

// Execute the function
queryMoviesByYear().catch(err => console.error('Execution error:', err));
