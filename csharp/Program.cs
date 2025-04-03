using System;
using System.Threading.Tasks;

namespace AmazonQCustomizationDemo
{
    class Program
    {
        static async Task Main(string[] args)
        {
            var generator = new Generator();
            await generator.GenerateFromCsv("movies.csv");
        }
    }
}
