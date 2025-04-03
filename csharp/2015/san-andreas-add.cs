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

            // Add "San Andreas" to the database
            // This demonstrates how to insert a new item into DynamoDB
            await movies.InsertAsync(
                title: "San Andreas",
                year: 2015,
                plot: "In the aftermath of a massive earthquake in California, a rescue-chopper pilot makes a dangerous journey with his ex-wife across the state in order to rescue his daughter.",
                rating: 6.1
            );

            // Confirm that the movie was added by retrieving it
            var movie = await movies.SelectAsync(
                title: "San Andreas",
                year: 2015
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
