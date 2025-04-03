import * as AWS from 'aws-sdk';
import { MovieRepository } from './MovieRepository';
import { Movie } from './Movie';

/**
 * Example demonstrating how to update a movie in DynamoDB using the MovieRepository class
 * 
 * This example shows:
 * 1. Creating a MovieRepository instance
 * 2. Checking if a movie exists
 * 3. Updating the movie's attributes if it exists
 */
async function updateMovie(): Promise<void> {
    // Configure AWS SDK (assuming credentials are set via environment variables or AWS config)
    AWS.config.update({ region: 'us-west-2' });
    
    // Create a MovieRepository instance
    const movies = new MovieRepository();
    
    try {
        // Check if the movie exists
        const movie = await movies.select({
            title: "Superbad",
            year: 2007
        });
        
        if (movie) {
            // The movie was found, so update it
            // This demonstrates how to update an existing item in DynamoDB
            const success = await movies.update({
                title: "Superbad",
                year: 2007,
                plot: "Two co-dependent high school seniors are forced to deal with separation anxiety after their plan to stage a booze-soaked party goes awry.",
                rating: 7.6
            });
            
            if (success) {
                console.log('Movie updated successfully');
            } else {
                console.log('Failed to update movie');
            }
        } else {
            // The movie was not found, so we cannot update
            console.log('Movie not found');
        }
    } catch (error) {
        console.error('Error updating movie:', error);
    }
}

// Execute the function
updateMovie().catch(err => console.error('Execution error:', err));
