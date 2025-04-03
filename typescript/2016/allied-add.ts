import * as AWS from 'aws-sdk';
import { MovieRepository } from './MovieRepository';
import { Movie } from './Movie';

/**
 * Example demonstrating how to add a movie to DynamoDB using the MovieRepository class
 * 
 * This example shows:
 * 1. Creating a MovieRepository instance
 * 2. Adding a new movie to the database
 * 3. Verifying the movie was added by retrieving it
 */
async function addMovie(): Promise<void> {
    // Configure AWS SDK (assuming credentials are set via environment variables or AWS config)
    AWS.config.update({ region: 'us-west-2' });
    
    // Create a MovieRepository instance
    const movies = new MovieRepository();
    
    try {
        // Add "Allied" to the database
        // This demonstrates how to insert a new item into DynamoDB
        const success = await movies.insert({
            title: "Allied",
            year: 2016,
            plot: "In 1942, a Canadian intelligence officer in North Africa encounters a female French Resistance fighter on a deadly mission behind enemy lines. When they reunite in London, their relationship is tested by the pressures of war.",
            rating: 7.1
        });
        
        if (success) {
            console.log('Movie added successfully');
            
            // Confirm that the movie was added by retrieving it
            const movie = await movies.select({
                title: "Allied",
                year: 2016
            });
            
            if (movie) {
                // The movie was found
                console.log('Movie found:', movie);
            } else {
                // The movie was not found
                console.log('Movie not found');
            }
        } else {
            console.log('Failed to add movie');
        }
    } catch (error) {
        console.error('Error adding movie:', error);
    }
}

// Execute the function
addMovie().catch(err => console.error('Execution error:', err));
