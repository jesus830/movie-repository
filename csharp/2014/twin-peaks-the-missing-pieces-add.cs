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

            // Add "Twin Peaks: The Missing Pieces" to the database
            // This demonstrates how to insert a new item into DynamoDB
            await movies.InsertAsync(
                title: "Twin Peaks: The Missing Pieces",
                year: 2014,
                plot: "Twin Peaks before Twin Peaks (1990) and at the same time not always and entirely in the same place as Twin Peaks: Fire Walk with Me (1992). A feature film which presents deleted scenes from Twin Peaks: Fire Walk with Me (1992) assembled together for the first time in an untold portion of the story's prequel.",
                rating: 8.1
            );

            // Confirm that the movie was added by retrieving it
            var movie = await movies.SelectAsync(
                title: "Twin Peaks: The Missing Pieces",
                year: 2014
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
