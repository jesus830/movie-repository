package com.example.moviedatabase;

import com.amazonaws.services.dynamodbv2.AmazonDynamoDB;
import com.amazonaws.services.dynamodbv2.AmazonDynamoDBClientBuilder;
import com.amazonaws.services.dynamodbv2.document.DynamoDB;
import com.amazonaws.services.dynamodbv2.document.Item;
import com.amazonaws.services.dynamodbv2.document.ItemCollection;
import com.amazonaws.services.dynamodbv2.document.QueryOutcome;
import com.amazonaws.services.dynamodbv2.document.Table;
import com.amazonaws.services.dynamodbv2.document.spec.QuerySpec;
import com.amazonaws.services.dynamodbv2.document.utils.ValueMap;
import java.util.Iterator;
import java.util.List;

/**
 * Example demonstrating how to query movies by year from DynamoDB using the MovieRepository class
 * 
 * This example shows:
 * 1. Creating a MovieRepository instance
 * 2. Querying for all movies from a specific year
 * 3. Processing the query results
 */
public class QueryMoviesByYear {

    public static void main(String[] args) {
        // Create a MovieRepository instance
        MovieRepository movies = new MovieRepository();
        
        try {
            // Query movies from 1972
            // This demonstrates how to query items using a secondary index
            List<Movie> results = movies.queryByYear(1972);
            
            System.out.println("Movies from 1972:");
            for (Movie movie : results) {
                System.out.println("- " + movie.getTitle() + " (Rating: " + movie.getRating() + ")");
            }
            
            System.out.println("Total movies found: " + results.size());
        } catch (Exception e) {
            System.err.println("Error querying movies: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
