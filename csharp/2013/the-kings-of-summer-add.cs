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

            // Add "The Kings of Summer" to the database
            // This demonstrates how to insert a new item into DynamoDB
            await movies.InsertAsync(
                title: "The Kings of Summer",
                year: 2013,
                plot: "Three teenage friends, in the ultimate act of independence, decide to spend their summer building a house in the woods and living off the land.",
                rating: 7.2
            );

            // Confirm that the movie was added by retrieving it
            var movie = await movies.SelectAsync(
                title: "The Kings of Summer",
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
