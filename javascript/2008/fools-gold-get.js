// Import required AWS SDK components
const AWS = require('aws-sdk');
const { MovieRepository } = require('./MovieRepository');

/**
 * Example demonstrating how to retrieve a movie from DynamoDB using the MovieRepository class
 * 
 * This example shows:
 * 1. Creating a MovieRepository instance
 * 2. Retrieving a movie by its primary key (title and year)
 * 3. Handling the case when a movie is found or not found
 */
async function getMovie() {
    // Configure AWS SDK (assuming credentials are set via environment variables or AWS config)
    AWS.config.update({ region: 'us-west-2' });
    
    // Create a MovieRepository instance
    const movies = new MovieRepository();
    
    try {
        // Retrieve the movie from DynamoDB
        // This demonstrates how to get an item by its primary key
        const movie = await movies.select({
            title: "Fool's Gold",
            year: 2008
        });
        
        if (movie) {
            // The movie was found
            console.log('Movie found:');
            console.log('Title:', movie.title);
            console.log('Year:', movie.year);
            console.log('Plot:', movie.plot);
            console.log('Rating:', movie.rating);
        } else {
            // The movie was not found
            console.log('Movie not found');
        }
    } catch (error) {
        console.error('Error retrieving movie:', error);
    }
}

// Execute the function
getMovie().catch(err => console.error('Execution error:', err));
