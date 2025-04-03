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

            // Add "The Green Inferno" to the database
            // This demonstrates how to insert a new item into DynamoDB
            await movies.InsertAsync(
                title: "The Green Inferno",
                year: 2013,
                plot: "A group of student activists travels to the Amazon to save the rain forest and soon discover that they are not alone, and that no good deed goes unpunished.",
                rating: 5.4
            );

            // Confirm that the movie was added by retrieving it
            var movie = await movies.SelectAsync(
                title: "The Green Inferno",
                year: 2013
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
