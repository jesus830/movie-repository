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
                title: "A Kind of Murder",
                year: 2016
            );

            if (movie != null)
            {
                // The movie was found, so update it
                // This demonstrates how to update an existing item in DynamoDB
                await movies.UpdateAsync(
                    title: "A Kind of Murder",
                    year: 2016,
                    plot: "In 1960s New York, Walter Stackhouse is a successful architect married to the beautiful Clara who leads a seemingly perfect life. But his fascination with an unsolved murder leads him into a spiral of chaos as he is forced to play cat-and-mouse with a clever killer and an overambitious detective, while at the same time lusting after another woman.",
                    rating: 5.2
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
