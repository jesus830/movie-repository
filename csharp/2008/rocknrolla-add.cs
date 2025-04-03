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

            // Add "RocknRolla" to the database
            // This demonstrates how to insert a new item into DynamoDB
            await movies.InsertAsync(
                title: "RocknRolla",
                year: 2008,
                plot: "In London, a real-estate scam puts millions of pounds up for grabs, attracting some of the city's scrappiest tough guys and its more established underworld types, all of whom are looking to get rich quick. While the city's seasoned criminals vie for the cash, an unexpected player -- a drugged-out rock 'n' roller presumed to be dead but very much alive -- has a multi-million-dollar prize fall into... See full summary »",
                rating: 7.3
            );

            // Confirm that the movie was added by retrieving it
            var movie = await movies.SelectAsync(
                title: "RocknRolla",
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
