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

            // Add "Demain tout commence" to the database
            // This demonstrates how to insert a new item into DynamoDB
            await movies.InsertAsync(
                title: "Demain tout commence",
                year: 2016,
                plot: "Samuel parties hard in the Marseille area of France and is awoken one morning by a woman carrying a baby she claims is his. She drives off leaving him with a wailing infant; he gives chase ... See full summary »",
                rating: 7.4
            );

            // Confirm that the movie was added by retrieving it
            var movie = await movies.SelectAsync(
                title: "Demain tout commence",
                year: 2016
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
