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

            // Add "Rock of Ages" to the database
            // This demonstrates how to insert a new item into DynamoDB
            await movies.InsertAsync(
                title: "Rock of Ages",
                year: 2012,
                plot: "A small town girl and a city boy meet on the Sunset Strip, while pursuing their Hollywood dreams.",
                rating: 5.9
            );

            // Confirm that the movie was added by retrieving it
            var movie = await movies.SelectAsync(
                title: "Rock of Ages",
                year: 2012
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
