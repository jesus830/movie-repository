// Import required AWS SDK components
const AWS = require('aws-sdk');
const { MovieRepository } = require('./MovieRepository');

/**
 * Example demonstrating how to add a movie to DynamoDB using the MovieRepository class
 * 
 * This example shows:
 * 1. Creating a MovieRepository instance
 * 2. Adding a new movie to the database
 * 3. Verifying the movie was added by retrieving it
 */
async function addMovie() {
    // Configure AWS SDK (assuming credentials are set via environment variables or AWS config)
    AWS.config.update({ region: 'us-west-2' });
    
    // Create a MovieRepository instance
    const movies = new MovieRepository();
    
    try {
        // Add "How to Train Your Dragon 2" to the database
        // This demonstrates how to insert a new item into DynamoDB
        const success = await movies.insert({
            title: "How to Train Your Dragon 2",
            year: 2014,
            plot: "When Hiccup and Toothless discover an ice cave that is home to hundreds of new wild dragons and the mysterious Dragon Rider, the two friends find themselves at the center of a battle to protect the peace.",
            rating: 7.9
        });
        
        if (success) {
            console.log('Movie added successfully');
            
            // Confirm that the movie was added by retrieving it
            const movie = await movies.select({
                title: "How to Train Your Dragon 2",
                year: 2014
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
