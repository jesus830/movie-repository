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

            // Retrieve the movie from DynamoDB
            // This demonstrates how to get an item by its primary key
            var movie = await movies.SelectAsync(
                title: "Superbad",
                year: 2007
            );

            if (movie != null)
            {
                // The movie was found
                Console.WriteLine("Movie found:");
                Console.WriteLine($"Title: {movie["title"]}");
                Console.WriteLine($"Year: {movie["year"]}");
                Console.WriteLine($"Plot: {movie["plot"]}");
                Console.WriteLine($"Rating: {movie["rating"]}");
            }
            else
            {
                // The movie was not found
                Console.WriteLine("Movie not found");
            }
        }
    }
}
