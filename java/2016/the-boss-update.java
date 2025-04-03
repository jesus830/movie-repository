package com.example.moviedatabase;

import com.amazonaws.services.dynamodbv2.AmazonDynamoDB;
import com.amazonaws.services.dynamodbv2.AmazonDynamoDBClientBuilder;
import com.amazonaws.services.dynamodbv2.document.DynamoDB;
import com.amazonaws.services.dynamodbv2.document.Table;
import com.amazonaws.services.dynamodbv2.document.UpdateItemOutcome;
import com.amazonaws.services.dynamodbv2.document.spec.UpdateItemSpec;
import com.amazonaws.services.dynamodbv2.document.utils.ValueMap;
import com.amazonaws.services.dynamodbv2.model.ReturnValue;

/**
 * Example demonstrating how to update a movie in DynamoDB using the MovieRepository class
 * 
 * This example shows:
 * 1. Creating a MovieRepository instance
 * 2. Checking if a movie exists
 * 3. Updating the movie's attributes if it exists
 */
public class UpdateMovie {

    public static void main(String[] args) {
        // Create a MovieRepository instance
        MovieRepository movies = new MovieRepository();
        
        try {
            // Check if the movie exists
            Movie movie = movies.select(
                "The Boss",    // title
                2016        // year
            );
            
            if (movie != null) {
                // The movie was found, so update it
                // This demonstrates how to update an existing item in DynamoDB
                boolean success = movies.update(
                    "The Boss",    // title
                    2016,       // year
                    "A titan of industry is sent to prison after she's caught insider trading. When she emerges ready to rebrand herself as America's latest sweetheart, not everyone she screwed over is so quick to forgive and forget.",     // plot
                    5.4      // rating
                );
                
                if (success) {
                    System.out.println("Movie updated successfully");
                } else {
                    System.out.println("Failed to update movie");
                }
            } else {
                // The movie was not found, so we cannot update
                System.out.println("Movie not found");
            }
        } catch (Exception e) {
            System.err.println("Error updating movie: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
