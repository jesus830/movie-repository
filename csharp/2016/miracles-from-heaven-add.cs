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

            // Add "Miracles from Heaven" to the database
            // This demonstrates how to insert a new item into DynamoDB
            await movies.InsertAsync(
                title: "Miracles from Heaven",
                year: 2016,
                plot: "A young girl suffering from a rare digestive disorder finds herself miraculously cured after surviving a terrible accident.",
                rating: 7
            );

            // Confirm that the movie was added by retrieving it
            var movie = await movies.SelectAsync(
                title: "Miracles from Heaven",
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
