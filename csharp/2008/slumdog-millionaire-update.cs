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

            // Check if the movie exists
            var movie = await movies.SelectAsync(
                title: "Slumdog Millionaire",
                year: 2008
            );

            if (movie != null)
            {
                // The movie was found, so update it
                // This demonstrates how to update an existing item in DynamoDB
                await movies.UpdateAsync(
                    title: "Slumdog Millionaire",
                    year: 2008,
                    plot: "A Mumbai teen reflects on his upbringing in the slums when he is accused of cheating on the Indian Version of 'Who Wants to be a Millionaire?'",
                    rating: 8
                );
                Console.WriteLine("Movie updated");
            }
            else
            {
                // The movie was not found, so we cannot update
                Console.WriteLine("Movie not found");
            }
        }
    }
}
