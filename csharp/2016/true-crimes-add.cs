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

            // Add "True Crimes" to the database
            // This demonstrates how to insert a new item into DynamoDB
            await movies.InsertAsync(
                title: "True Crimes",
                year: 2016,
                plot: "A murder investigation of a slain business man turns to clues found in an author's book about an eerily similar crime. Based on the 2008 article 'True Crimes - A postmodern murder mystery' by David Grann.",
                rating: 7.3
            );

            // Confirm that the movie was added by retrieving it
            var movie = await movies.SelectAsync(
                title: "True Crimes",
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
