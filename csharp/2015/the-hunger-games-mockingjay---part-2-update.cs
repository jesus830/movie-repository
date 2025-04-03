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
                title: "The Hunger Games: Mockingjay - Part 2",
                year: 2015
            );

            if (movie != null)
            {
                // The movie was found, so update it
                // This demonstrates how to update an existing item in DynamoDB
                await movies.UpdateAsync(
                    title: "The Hunger Games: Mockingjay - Part 2",
                    year: 2015,
                    plot: "As the war of Panem escalates to the destruction of other districts, Katniss Everdeen, the reluctant leader of the rebellion, must bring together an army against President Snow, while all she holds dear hangs in the balance.",
                    rating: 6.6
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
