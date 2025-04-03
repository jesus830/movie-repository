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

            // Add "In Dubious Battle" to the database
            // This demonstrates how to insert a new item into DynamoDB
            await movies.InsertAsync(
                title: "In Dubious Battle",
                year: 2016,
                plot: "An activist gets caught up in the labor movement for farm workers in California during the 1930s.",
                rating: 6.2
            );

            // Confirm that the movie was added by retrieving it
            var movie = await movies.SelectAsync(
                title: "In Dubious Battle",
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
