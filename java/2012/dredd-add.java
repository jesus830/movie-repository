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
            // Add "Dredd" to the database
            // This demonstrates how to insert a new item into DynamoDB
            boolean success = movies.insert(
                "Dredd",    // title
                2012,       // year
                "In a violent, futuristic city where the police have the authority to act as judge, jury and executioner, a cop teams with a trainee to take down a gang that deals the reality-altering drug, SLO-MO.",     // plot
                7.1      // rating
            );
            
            if (success) {
                System.out.println("Movie added successfully");
                
                // Confirm that the movie was added by retrieving it
                Movie movie = movies.select(
                    "Dredd",    // title
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
