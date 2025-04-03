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
                title: "King Cobra",
                year: 2016
            );

            if (movie != null)
            {
                // The movie was found, so update it
                // This demonstrates how to update an existing item in DynamoDB
                await movies.UpdateAsync(
                    title: "King Cobra",
                    year: 2016,
                    plot: "This ripped-from-the-headlines drama covers the early rise of gay porn headliner Sean Paul Lockhart a.k.a. Brent Corrigan, before his falling out with the producer who made him famous. When... See full summary »",
                    rating: 5.6
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
