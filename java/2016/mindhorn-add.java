package com.example.moviedatabase;

import com.amazonaws.services.dynamodbv2.AmazonDynamoDB;
import com.amazonaws.services.dynamodbv2.AmazonDynamoDBClientBuilder;
import com.amazonaws.services.dynamodbv2.document.DynamoDB;
import com.amazonaws.services.dynamodbv2.document.Item;
import com.amazonaws.services.dynamodbv2.document.Table;
import com.amazonaws.services.dynamodbv2.document.spec.GetItemSpec;

/**
 * Example demonstrating how to add a movie to DynamoDB using the MovieRepository class
 * 
 * This example shows:
 * 1. Creating a MovieRepository instance
 * 2. Adding a new movie to the database
 * 3. Verifying the movie was added by retrieving it
 */
public class AddMovie {

    public static void main(String[] args) {
        // Create a MovieRepository instance
        MovieRepository movies = new MovieRepository();
        
        try {
            // Add "Mindhorn" to the database
            // This demonstrates how to insert a new item into DynamoDB
            boolean success = movies.insert(
                "Mindhorn",    // title
                2016,       // year
                "A has-been actor best known for playing the title character in the 1980s detective series 'Mindhorn' must work with the police when a serial killer says that he will only speak with Detective Mindhorn, whom he believes to be a real person.",     // plot
                6.4      // rating
            );
            
            if (success) {
                System.out.println("Movie added successfully");
                
                // Confirm that the movie was added by retrieving it
                Movie movie = movies.select(
                    "Mindhorn",    // title
                    2016        // year
                );
                
                if (movie != null) {
                    // The movie was found
                    System.out.println("Movie found: " + movie.toString());
                } else {
                    // The movie was not found
                    System.out.println("Movie not found");
                }
            } else {
                System.out.println("Failed to add movie");
            }
        } catch (Exception e) {
            System.err.println("Error adding movie: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
