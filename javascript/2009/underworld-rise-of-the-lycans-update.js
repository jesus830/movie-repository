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
            title: "Underworld: Rise of the Lycans",
            year: 2009
        });
        
        if (movie) {
            // The movie was found, so update it
            // This demonstrates how to update an existing item in DynamoDB
            const success = await movies.update({
                title: "Underworld: Rise of the Lycans",
                year: 2009,
                plot: "An origins story centered on the centuries-old feud between the race of aristocratic vampires and their onetime slaves, the Lycans.",
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
