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

            // Query movies from 1972
            // This demonstrates how to query items using a secondary index
            var results = await movies.QueryByYearAsync(1972);

            Console.WriteLine($"Movies from 1972:");
            foreach (var movie in results)
            {
                Console.WriteLine($"- {movie["title"]} (Rating: {movie["rating"]})");
            }
        }
    }
}
