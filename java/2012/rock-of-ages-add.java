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
            // Add "Rock of Ages" to the database
            // This demonstrates how to insert a new item into DynamoDB
            boolean success = movies.insert(
                "Rock of Ages",    // title
                2012,       // year
                "A small town girl and a city boy meet on the Sunset Strip, while pursuing their Hollywood dreams.",     // plot
                5.9      // rating
            );
            
            if (success) {
                System.out.println("Movie added successfully");
                
                // Confirm that the movie was added by retrieving it
                Movie movie = movies.select(
                    "Rock of Ages",    // title
                    2012        // year
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
