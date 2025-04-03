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
                title: "Exodus: Gods and Kings",
                year: 2014
            );

            if (movie != null)
            {
                // The movie was found, so update it
                // This demonstrates how to update an existing item in DynamoDB
                await movies.UpdateAsync(
                    title: "Exodus: Gods and Kings",
                    year: 2014,
                    plot: "The defiant leader Moses rises up against the Egyptian Pharaoh Ramses, setting 600,000 slaves on a monumental journey of escape from Egypt and its terrifying cycle of deadly plagues.",
                    rating: 6
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
