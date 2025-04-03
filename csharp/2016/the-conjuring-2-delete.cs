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

            // Confirm that the movie exists in the database
            var movie = await movies.SelectAsync(
                title: "The Conjuring 2",
                year: 2016
            );

            if (movie != null)
            {
                // Delete the movie
                // This demonstrates how to remove an item from DynamoDB
                Console.WriteLine("Deleting movie");
                await movies.DeleteAsync(
                    title: "The Conjuring 2",
                    year: 2016
                );
            }
            else
            {
                // Warn that the movie doesn't exist
                Console.WriteLine("Movie not found; therefore, no need to delete it.");
            }
        }
    }
}
