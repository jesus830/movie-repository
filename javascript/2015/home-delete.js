// Import required AWS SDK components
const AWS = require('aws-sdk');
const { MovieRepository } = require('./MovieRepository');

/**
 * Example demonstrating how to delete a movie from DynamoDB using the MovieRepository class
 * 
 * This example shows:
 * 1. Creating a MovieRepository instance
 * 2. Checking if a movie exists
 * 3. Deleting the movie if it exists
 */
async function deleteMovie() {
    // Configure AWS SDK (assuming credentials are set via environment variables or AWS config)
    AWS.config.update({ region: 'us-west-2' });
    
    // Create a MovieRepository instance
    const movies = new MovieRepository();
    
    try {
        // Confirm that the movie exists in the database
        const movie = await movies.select({
            title: "Home",
            year: 2015
        });
        
        if (movie) {
            // Delete the movie
            // This demonstrates how to remove an item from DynamoDB
            console.log('Deleting movie');
            const success = await movies.delete({
                title: "Home",
                year: 2015
            });
            
            if (success) {
                console.log('Movie deleted successfully');
            } else {
                console.log('Failed to delete movie');
            }
        } else {
            // Warn that the movie doesn't exist
            console.log('Movie not found; therefore, no need to delete it.');
        }
    } catch (error) {
        console.error('Error deleting movie:', error);
    }
}

// Execute the function
deleteMovie().catch(err => console.error('Execution error:', err));
