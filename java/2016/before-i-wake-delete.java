package com.example.moviedatabase;

import com.amazonaws.services.dynamodbv2.AmazonDynamoDB;
import com.amazonaws.services.dynamodbv2.AmazonDynamoDBClientBuilder;
import com.amazonaws.services.dynamodbv2.document.DynamoDB;
import com.amazonaws.services.dynamodbv2.document.Table;

/**
 * Example demonstrating how to delete a movie from DynamoDB using the MovieRepository class
 * 
 * This example shows:
 * 1. Creating a MovieRepository instance
 * 2. Checking if a movie exists
 * 3. Deleting the movie if it exists
 */
public class DeleteMovie {

    public static void main(String[] args) {
        // Create a MovieRepository instance
        MovieRepository movies = new MovieRepository();
        
        try {
            // Confirm that the movie exists in the database
            Movie movie = movies.select(
                "Before I Wake",    // title
                2016        // year
            );
            
            if (movie != null) {
                // Delete the movie
                // This demonstrates how to remove an item from DynamoDB
                System.out.println("Deleting movie");
                boolean success = movies.delete(
                    "Before I Wake",    // title
                    2016        // year
                );
                
                if (success) {
                    System.out.println("Movie deleted successfully");
                } else {
                    System.out.println("Failed to delete movie");
                }
            } else {
                // Warn that the movie doesn't exist
                System.out.println("Movie not found; therefore, no need to delete it.");
            }
        } catch (Exception e) {
            System.err.println("Error deleting movie: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
