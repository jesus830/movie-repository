using System;
using System.Threading.Tasks;
using Amazon.DynamoDBv2;
using Amazon.DynamoDBv2.Model;
using System.Collections.Generic;

namespace MovieDatabase
{
    class Program
    {
        static async Task Main(string[] args)
        {
            // Create a MovieRepository instance
            var movies = new MovieRepository();

            // Add "The Gambler" to the database
            // This demonstrates how to insert a new item into DynamoDB
            await movies.InsertAsync(
                title: "The Gambler",
                year: 2014,
                plot: "Lit professor and gambler Jim Bennett's debt causes him to borrow money from his mother and a loan shark. Further complicating his situation is his relationship with one of his students. Will Bennett risk his life for a second chance?",
                rating: 6
            );

            // Confirm that the movie was added by retrieving it
            var movie = await movies.SelectAsync(
                title: "The Gambler",
                year: 2014
            );

            if (movie != null)
            {
                // The movie was found
                Console.WriteLine($"Movie found: {movie}");
            }
            else
            {
                // The movie was not found
                Console.WriteLine("Movie not found");
            }
        }
    }
}
