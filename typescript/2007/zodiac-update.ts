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
            title: "Zodiac",
            year: 2007
        });
        
        if (movie) {
            // The movie was found, so update it
            // This demonstrates how to update an existing item in DynamoDB
            const success = await movies.update({
                title: "Zodiac",
                year: 2007,
                plot: "In the late 1960s/early 1970s, a San Francisco cartoonist becomes an amateur detective obsessed with tracking down the Zodiac Killer, an unidentified individual who terrorizes Northern California with a killing spree.",
                rating: 7.7
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
