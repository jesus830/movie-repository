package com.example.moviedatabase;

import com.amazonaws.services.dynamodbv2.AmazonDynamoDB;
import com.amazonaws.services.dynamodbv2.AmazonDynamoDBClientBuilder;
import com.amazonaws.services.dynamodbv2.document.DynamoDB;
import com.amazonaws.services.dynamodbv2.document.Item;
import com.amazonaws.services.dynamodbv2.document.Table;
import com.amazonaws.services.dynamodbv2.document.spec.GetItemSpec;

/**
 * Example demonstrating how to retrieve a movie from DynamoDB using the MovieRepository class
 * 
 * This example shows:
 * 1. Creating a MovieRepository instance
 * 2. Retrieving a movie by its primary key (title and year)
 * 3. Handling the case when a movie is found or not found
 */
public class GetMovie {

    public static void main(String[] args) {
        // Create a MovieRepository instance
        MovieRepository movies = new MovieRepository();
        
        try {
            // Retrieve the movie from DynamoDB
            // This demonstrates how to get an item by its primary key
            Movie movie = movies.select(
                "The Ticket",    // title
                2016        // year
            );
            
            if (movie != null) {
                // The movie was found
                System.out.println("Movie found:");
                System.out.println("Title: " + movie.getTitle());
                System.out.println("Year: " + movie.getYear());
                System.out.println("Plot: " + movie.getPlot());
                System.out.println("Rating: " + movie.getRating());
            } else {
                // The movie was not found
                System.out.println("Movie not found");
            }
        } catch (Exception e) {
            System.err.println("Error retrieving movie: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
