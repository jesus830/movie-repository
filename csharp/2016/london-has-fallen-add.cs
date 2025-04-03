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

            // Add "London Has Fallen" to the database
            // This demonstrates how to insert a new item into DynamoDB
            await movies.InsertAsync(
                title: "London Has Fallen",
                year: 2016,
                plot: "In London for the Prime Minister's funeral, Mike Banning discovers a plot to assassinate all the attending world leaders.",
                rating: 5.9
            );

            // Confirm that the movie was added by retrieving it
            var movie = await movies.SelectAsync(
                title: "London Has Fallen",
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
