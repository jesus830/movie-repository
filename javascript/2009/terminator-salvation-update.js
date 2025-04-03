// Import required AWS SDK components
const AWS = require('aws-sdk');
const { MovieRepository } = require('./MovieRepository');

/**
 * Example demonstrating how to update a movie in DynamoDB using the MovieRepository class
 * 
 * This example shows:
 * 1. Creating a MovieRepository instance
 * 2. Checking if a movie exists
 * 3. Updating the movie's attributes if it exists
 */
async function updateMovie() {
    // Configure AWS SDK (assuming credentials are set via environment variables or AWS config)
    AWS.config.update({ region: 'us-west-2' });
    
    // Create a MovieRepository instance
    const movies = new MovieRepository();
    
    try {
        // Check if the movie exists
        const movie = await movies.select({
            title: "Terminator Salvation",
            year: 2009
        });
        
        if (movie) {
            // The movie was found, so update it
            // This demonstrates how to update an existing item in DynamoDB
            const success = await movies.update({
                title: "Terminator Salvation",
                year: 2009,
                plot: "In 2018, a mysterious new weapon in the war against the machines, half-human and half-machine, comes to John Connor on the eve of a resistance attack on Skynet. But whose side is he on, and can he be trusted?",
                rating: 6.6
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
