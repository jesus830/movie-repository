# C# DynamoDB Movie Database

## Overview

This C# implementation provides a robust and feature-rich interface for managing a movie database using Amazon DynamoDB. The `MovieRepository` class encapsulates all the functionality needed to create, read, update, and delete movie data, as well as perform queries and scans across the database.

## Installation

### Prerequisites

- .NET Core 3.1 or .NET 5.0+ SDK
- AWS account with appropriate permissions
- AWS credentials configured locally

### NuGet Packages

Add the following NuGet packages to your project:

```bash
dotnet add package AWSSDK.DynamoDBv2
dotnet add package AWSSDK.Extensions.NETCore.Setup
```

Or add them to your `.csproj` file:

```xml
<ItemGroup>
  <PackageReference Include="AWSSDK.DynamoDBv2" Version="3.7.100.16" />
  <PackageReference Include="AWSSDK.Extensions.NETCore.Setup" Version="3.7.7" />
</ItemGroup>
```

### AWS Configuration

1. Install the AWS CLI:
   ```bash
   dotnet tool install -g Amazon.Lambda.Tools
   ```

2. Configure your AWS credentials:
   ```bash
   aws configure
   ```

3. Or add configuration to your `appsettings.json`:
   ```json
   {
     "AWS": {
       "Profile": "default",
       "Region": "us-west-2"
     }
   }
   ```

## Usage

### Initializing the Repository

```csharp
using AmazonQCustomizationDemo;
using Amazon.DynamoDBv2;

// Initialize with default settings (uses "Movies" table)
var repo = new MovieRepository();

// Or specify a custom table name
var repo = new MovieRepository(tableName: "CustomMoviesTable");

// Or provide your own DynamoDB client
var client = new AmazonDynamoDBClient(RegionEndpoint.USWest2);
var repo = new MovieRepository(client, "CustomMoviesTable");
```

### Dependency Injection Setup

```csharp
// In Startup.cs
public void ConfigureServices(IServiceCollection services)
{
    services.AddAWSService<IAmazonDynamoDB>();
    services.AddSingleton<MovieRepository>();
}
```

### Creating a Table

```csharp
// Create a new table if it doesn't exist
if (!await repo.Exists("Movies"))
{
    var table = await repo.CreateTable("Movies");
    Console.WriteLine($"Table created: {table.TableName}");
}
```

### Adding Movies

```csharp
// Add a single movie
await repo.Insert(
    title: "The Matrix",
    year: 1999,
    plot: "A computer hacker learns about the true nature of reality.",
    rating: 8.7m
);

// Add multiple movies using batch write
var movies = new List<Document>
{
    new Document
    {
        ["year"] = 1994,
        ["title"] = "The Shawshank Redemption",
        ["info"] = new Document
        {
            ["plot"] = "Two imprisoned men bond over a number of years.",
            ["rating"] = 9.3m
        }
    },
    new Document
    {
        ["year"] = 1972,
        ["title"] = "The Godfather",
        ["info"] = new Document
        {
            ["plot"] = "The aging patriarch of an organized crime dynasty transfers control to his son.",
            ["rating"] = 9.2m
        }
    }
};
await repo.WriteBatch(movies);
```

### Retrieving Movies

```csharp
// Get a specific movie by title and year
var movie = await repo.Select("The Matrix", 1999);
Console.WriteLine($"Title: {movie["title"]}");
Console.WriteLine($"Year: {movie["year"]}");
Console.WriteLine($"Plot: {movie["info"]["plot"]}");
Console.WriteLine($"Rating: {movie["info"]["rating"]}");
```

### Updating Movies

```csharp
// Update a movie's plot and rating
var updated = await repo.Update(
    title: "The Matrix",
    year: 1999,
    plot: "A computer programmer discovers a dystopian world is actually a simulation.",
    rating: 9.0m
);
Console.WriteLine("Updated attributes: " + string.Join(", ", updated.Keys));
```

### Querying Movies

```csharp
// Find all movies released in 1999
var movies1999 = await repo.QueryMovies(1999);
Console.WriteLine($"Found {movies1999.Count} movies from 1999:");
foreach (var movie in movies1999)
{
    Console.WriteLine($"- {movie["title"]}: {movie["info"]["rating"]}");
}
```

### Scanning Movies

```csharp
// Find all movies released between 1990 and 1999
var ninetiesMovies = await repo.ScanMovies(1990, 1999);
Console.WriteLine($"Found {ninetiesMovies.Count} movies from the 90s:");
foreach (var movie in ninetiesMovies)
{
    Console.WriteLine($"- {movie["title"]} ({movie["year"]}): {movie["info"]["rating"]}");
}
```

### Deleting Movies

```csharp
// Delete a specific movie
await repo.Delete("The Matrix", 1999);
Console.WriteLine("Movie deleted successfully");
```

### Deleting the Table

```csharp
// Delete the entire table when no longer needed
await repo.DeleteTable();
Console.WriteLine("Table deleted successfully");
```

## Advanced Usage

### Listing Tables

```csharp
// List all DynamoDB tables in your account
var tables = await repo.ListTables();
Console.WriteLine("Available tables: " + string.Join(", ", tables));
```

### Asynchronous Operations

All methods in the `MovieRepository` class are asynchronous and return `Task` or `Task<T>`, making them ideal for modern C# applications:

```csharp
// Perform multiple operations concurrently
var task1 = repo.QueryMovies(1999);
var task2 = repo.QueryMovies(2000);
await Task.WhenAll(task1, task2);

var movies1999 = await task1;
var movies2000 = await task2;
Console.WriteLine($"Found {movies1999.Count} movies from 1999 and {movies2000.Count} movies from 2000");
```

### Error Handling

```csharp
try
{
    await repo.Select("Non-existent Movie", 2099);
}
catch (Amazon.DynamoDBv2.Model.ResourceNotFoundException)
{
    Console.WriteLine("Movie not found");
}
catch (Exception ex)
{
    Console.WriteLine($"Error retrieving movie: {ex.Message}");
}
```

## Troubleshooting

### Common Issues

1. **AWS Credentials Not Found**

   Ensure your credentials are properly configured in `~/.aws/credentials`:
   ```ini
   [default]
   aws_access_key_id = YOUR_ACCESS_KEY
   aws_secret_access_key = YOUR_SECRET_KEY
   ```

   Or set them in environment variables:
   ```bash
   export AWS_ACCESS_KEY_ID=YOUR_ACCESS_KEY
   export AWS_SECRET_ACCESS_KEY=YOUR_SECRET_KEY
   ```

2. **Table Already Exists**

   Handle the ResourceInUseException:
   ```csharp
   try
   {
       await repo.CreateTable("Movies");
   }
   catch (Amazon.DynamoDBv2.Model.ResourceInUseException)
   {
       Console.WriteLine("Table already exists");
   }
   ```

3. **Provisioned Throughput Exceeded**

   Implement exponential backoff:
   ```csharp
   int retries = 0;
   while (retries < 3)
   {
       try
       {
           await repo.Insert(title, year, plot, rating);
           break;
       }
       catch (Amazon.DynamoDBv2.Model.ProvisionedThroughputExceededException)
       {
           retries++;
           await Task.Delay((int)Math.Pow(2, retries) * 100);
       }
   }
   ```

### Logging

Configure logging with the built-in .NET Core logging:

```csharp
// In Program.cs or Startup.cs
public static IHostBuilder CreateHostBuilder(string[] args) =>
    Host.CreateDefaultBuilder(args)
        .ConfigureLogging(logging =>
        {
            logging.ClearProviders();
            logging.AddConsole();
            logging.AddDebug();
            logging.SetMinimumLevel(LogLevel.Information);
        });
```

## Performance Optimization

### Connection Pooling

The AWS SDK for .NET automatically manages connection pooling, but you can configure it:

```csharp
var config = new AmazonDynamoDBConfig
{
    RegionEndpoint = RegionEndpoint.USWest2,
    MaxConnectionsPerServer = 100,
    Timeout = TimeSpan.FromSeconds(10)
};
var client = new AmazonDynamoDBClient(config);
var repo = new MovieRepository(client);
```

### Batch Processing

For large datasets, use the batch write functionality with appropriate chunking:

```csharp
var largeMovieList = new List<Document>(); // ... large list of movies ...
const int batchSize = 25; // DynamoDB batch write limit

for (int i = 0; i < largeMovieList.Count; i += batchSize)
{
    var batch = largeMovieList.Skip(i).Take(batchSize).ToList();
    await repo.WriteBatch(batch);
}
```

## API Reference

### Constructor

- `MovieRepository(IAmazonDynamoDB dynamoDbClient = null, string tableName = "Movies")`: Initializes a new repository instance.

### Table Operations

- `Task<bool> Exists(string tableName)`: Checks if a table exists.
- `Task<Table> CreateTable(string tableName)`: Creates a new table.
- `Task<List<string>> ListTables()`: Lists all tables.
- `Task DeleteTable()`: Deletes the table.

### Item Operations

- `Task Insert(string title, int year, string plot, decimal rating)`: Adds a new movie.
- `Task<Document> Select(string title, int year)`: Retrieves a specific movie.
- `Task<Document> Update(string title, int year, string plot, decimal rating)`: Updates a movie's details.
- `Task Delete(string title, int year)`: Deletes a specific movie.

### Query Operations

- `Task<List<Document>> QueryMovies(int year)`: Finds movies from a specific year.
- `Task<List<Document>> ScanMovies(int firstYear, int secondYear)`: Finds movies within a year range.
- `Task WriteBatch(List<Document> movies)`: Adds multiple movies in a batch.

## Unit Testing

Example of unit testing the repository with xUnit and Moq:

```csharp
public class MovieRepositoryTests
{
    private readonly Mock<IAmazonDynamoDB> _mockDynamoDb;
    private readonly MovieRepository _repository;

    public MovieRepositoryTests()
    {
        _mockDynamoDb = new Mock<IAmazonDynamoDB>();
        _repository = new MovieRepository(_mockDynamoDb.Object, "TestMovies");
    }

    [Fact]
    public async Task Insert_ShouldCallPutItem()
    {
        // Arrange
        _mockDynamoDb.Setup(m => m.PutItemAsync(
            It.IsAny<PutItemRequest>(),
            It.IsAny<CancellationToken>()))
            .ReturnsAsync(new PutItemResponse());

        // Act
        await _repository.Insert("Test Movie", 2023, "Test plot", 8.5m);

        // Assert
        _mockDynamoDb.Verify(m => m.PutItemAsync(
            It.Is<PutItemRequest>(r => 
                r.TableName == "TestMovies" && 
                r.Item["title"].S == "Test Movie" &&
                r.Item["year"].N == "2023"),
            It.IsAny<CancellationToken>()),
            Times.Once);
    }
}
```

## Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
