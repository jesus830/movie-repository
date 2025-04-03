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

            // Add "The Boy in the Striped Pyjamas" to the database
            // This demonstrates how to insert a new item into DynamoDB
            await movies.InsertAsync(
                title: "The Boy in the Striped Pyjamas",
                year: 2008,
                plot: "Set during WWII, a story seen through the innocent eyes of Bruno, the eight-year-old son of the commandant at a German concentration camp, whose forbidden friendship with a Jewish boy on the other side of the camp fence has startling and unexpected consequences.",
                rating: 7.8
            );

            // Confirm that the movie was added by retrieving it
            var movie = await movies.SelectAsync(
                title: "The Boy in the Striped Pyjamas",
                year: 2008
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
