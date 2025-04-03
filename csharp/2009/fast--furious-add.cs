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

            // Add "Fast & Furious" to the database
            // This demonstrates how to insert a new item into DynamoDB
            await movies.InsertAsync(
                title: "Fast & Furious",
                year: 2009,
                plot: "Brian O'Conner, back working for the FBI in Los Angeles, teams up with Dominic Toretto to bring down a heroin importer by infiltrating his operation.",
                rating: 6.6
            );

            // Confirm that the movie was added by retrieving it
            var movie = await movies.SelectAsync(
                title: "Fast & Furious",
                year: 2009
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
