# C++ DynamoDB Movie Database

## Overview

This C++ implementation provides a powerful and efficient interface for managing a movie database using Amazon DynamoDB. The `MovieRepository` class encapsulates all the functionality needed to create, read, update, and delete movie data, as well as perform queries and scans across the database.

## Installation

### Prerequisites

- C++11 compatible compiler (GCC 4.9+, Clang 3.4+, MSVC 2015+)
- CMake 3.9 or higher
- AWS SDK for C++ (aws-sdk-cpp)
- AWS account with appropriate permissions
- AWS credentials configured locally

### Building the AWS SDK for C++

1. Clone the AWS SDK for C++ repository:
   ```bash
   git clone https://github.com/aws/aws-sdk-cpp.git
   cd aws-sdk-cpp
   ```

2. Create a build directory:
   ```bash
   mkdir build
   cd build
   ```

3. Configure with CMake (minimal build with only DynamoDB):
   ```bash
   cmake .. -DBUILD_ONLY="dynamodb" -DCMAKE_BUILD_TYPE=Release
   ```

4. Build and install:
   ```bash
   make
   sudo make install
   ```

### Building the Movie Database Application

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/amazon-q-customization-demo-python.git
   cd amazon-q-customization-demo-python/cpp
   ```

2. Create a build directory:
   ```bash
   mkdir build
   cd build
   ```

3. Configure with CMake:
   ```bash
   cmake ..
   ```

4. Build:
   ```bash
   make
   ```

### AWS Configuration

1. Install the AWS CLI:
   ```bash
   pip install awscli
   ```

2. Configure your AWS credentials:
   ```bash
   aws configure
   ```

3. Or create credentials file manually:
   ```bash
   mkdir -p ~/.aws
   touch ~/.aws/credentials
   ```

   Add your credentials to the file:
   ```ini
   [default]
   aws_access_key_id = YOUR_ACCESS_KEY
   aws_secret_access_key = YOUR_SECRET_KEY
   ```

## Usage

### Initializing the Repository

```cpp
#include "MovieRepository.h"

// Initialize with default settings (uses "Movies" table)
Aws::SDKOptions options;
Aws::InitAPI(options);
{
    MovieRepository repo;
    
    // Use the repository...
    
} // Repository will be destroyed here
Aws::ShutdownAPI(options);

// Or specify a custom client and table name
Aws::Client::ClientConfiguration clientConfig;
clientConfig.region = Aws::Region::US_WEST_2;
auto dynamoClient = Aws::MakeShared<Aws::DynamoDB::DynamoDBClient>(
    "DynamoDBClient", clientConfig);
MovieRepository repo(dynamoClient, "CustomMoviesTable");
```

### Creating a Table

```cpp
// Create a new table if it doesn't exist
if (!repo.Exists("Movies")) {
    auto outcome = repo.CreateTable("Movies");
    if (outcome.IsSuccess()) {
        std::cout << "Table created successfully" << std::endl;
    } else {
        std::cerr << "Failed to create table: " 
                  << outcome.GetError().GetMessage() << std::endl;
    }
}
```

### Adding Movies

```cpp
// Add a single movie
repo.Insert(
    "The Matrix",
    1999,
    "A computer hacker learns about the true nature of reality.",
    8.7
);

// Add multiple movies using batch write
std::vector<Aws::Map<Aws::String, Aws::DynamoDB::Model::AttributeValue>> movies;

// First movie
Aws::Map<Aws::String, Aws::DynamoDB::Model::AttributeValue> movie1;
movie1["year"].SetN("1994");
movie1["title"].SetS("The Shawshank Redemption");

Aws::Map<Aws::String, Aws::DynamoDB::Model::AttributeValue> info1;
info1["plot"].SetS("Two imprisoned men bond over a number of years.");
info1["rating"].SetN("9.3");
movie1["info"].SetM(info1);
movies.push_back(movie1);

// Second movie
Aws::Map<Aws::String, Aws::DynamoDB::Model::AttributeValue> movie2;
movie2["year"].SetN("1972");
movie2["title"].SetS("The Godfather");

Aws::Map<Aws::String, Aws::DynamoDB::Model::AttributeValue> info2;
info2["plot"].SetS("The aging patriarch of an organized crime dynasty transfers control to his son.");
info2["rating"].SetN("9.2");
movie2["info"].SetM(info2);
movies.push_back(movie2);

repo.WriteBatch(movies);
```

### Retrieving Movies

```cpp
// Get a specific movie by title and year
auto outcome = repo.Select("The Matrix", 1999);
if (outcome.IsSuccess()) {
    const auto& item = outcome.GetResult().GetItem();
    std::cout << "Title: " << item.at("title").GetS() << std::endl;
    std::cout << "Year: " << item.at("year").GetN() << std::endl;
    
    const auto& info = item.at("info").GetM();
    std::cout << "Plot: " << info.at("plot").GetS() << std::endl;
    std::cout << "Rating: " << info.at("rating").GetN() << std::endl;
} else {
    std::cerr << "Failed to get movie: " 
              << outcome.GetError().GetMessage() << std::endl;
}
```

### Updating Movies

```cpp
// Update a movie's plot and rating
auto outcome = repo.Update(
    "The Matrix",
    1999,
    "A computer programmer discovers a dystopian world is actually a simulation.",
    9.0
);
if (outcome.IsSuccess()) {
    std::cout << "Movie updated successfully" << std::endl;
    
    const auto& attributes = outcome.GetResult().GetAttributes();
    for (const auto& attr : attributes) {
        std::cout << "Updated: " << attr.first << std::endl;
    }
} else {
    std::cerr << "Failed to update movie: " 
              << outcome.GetError().GetMessage() << std::endl;
}
```

### Querying Movies

```cpp
// Find all movies released in 1999
auto outcome = repo.QueryMovies(1999);
if (outcome.IsSuccess()) {
    const auto& items = outcome.GetResult().GetItems();
    std::cout << "Found " << items.size() << " movies from 1999:" << std::endl;
    
    for (const auto& item : items) {
        std::cout << "- " << item.at("title").GetS() << ": " 
                  << item.at("info").GetM().at("rating").GetN() << std::endl;
    }
} else {
    std::cerr << "Failed to query movies: " 
              << outcome.GetError().GetMessage() << std::endl;
}
```

### Scanning Movies

```cpp
// Find all movies released between 1990 and 1999
auto outcome = repo.ScanMovies(1990, 1999);
if (outcome.IsSuccess()) {
    const auto& items = outcome.GetResult().GetItems();
    std::cout << "Found " << items.size() << " movies from the 90s:" << std::endl;
    
    for (const auto& item : items) {
        std::cout << "- " << item.at("title").GetS() 
                  << " (" << item.at("year").GetN() << "): " 
                  << item.at("info").GetM().at("rating").GetN() << std::endl;
    }
} else {
    std::cerr << "Failed to scan movies: " 
              << outcome.GetError().GetMessage() << std::endl;
}
```

### Deleting Movies

```cpp
// Delete a specific movie
auto outcome = repo.Delete("The Matrix", 1999);
if (outcome.IsSuccess()) {
    std::cout << "Movie deleted successfully" << std::endl;
} else {
    std::cerr << "Failed to delete movie: " 
              << outcome.GetError().GetMessage() << std::endl;
}
```

### Deleting the Table

```cpp
// Delete the entire table when no longer needed
auto outcome = repo.DeleteTable();
if (outcome.IsSuccess()) {
    std::cout << "Table deleted successfully" << std::endl;
} else {
    std::cerr << "Failed to delete table: " 
              << outcome.GetError().GetMessage() << std::endl;
}
```

## Advanced Usage

### Listing Tables

```cpp
// List all DynamoDB tables in your account
auto outcome = repo.ListTables();
if (outcome.IsSuccess()) {
    const auto& tables = outcome.GetResult().GetTableNames();
    std::cout << "Available tables:" << std::endl;
    for (const auto& table : tables) {
        std::cout << "- " << table << std::endl;
    }
} else {
    std::cerr << "Failed to list tables: " 
              << outcome.GetError().GetMessage() << std::endl;
}
```

### Error Handling

```cpp
try {
    auto outcome = repo.Select("Non-existent Movie", 2099);
    if (!outcome.IsSuccess()) {
        const auto& error = outcome.GetError();
        std::cerr << "Error: " << error.GetExceptionName() << " - " 
                  << error.GetMessage() << std::endl;
    }
} catch (const std::exception& e) {
    std::cerr << "Exception: " << e.what() << std::endl;
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
   ```cpp
   auto outcome = repo.CreateTable("Movies");
   if (!outcome.IsSuccess()) {
       const auto& error = outcome.GetError();
       if (error.GetExceptionName() == "ResourceInUseException") {
           std::cout << "Table already exists" << std::endl;
       } else {
           std::cerr << "Error: " << error.GetMessage() << std::endl;
       }
   }
   ```

3. **Provisioned Throughput Exceeded**

   Implement exponential backoff:
   ```cpp
   int retries = 0;
   bool success = false;
   while (retries < 3 && !success) {
       auto outcome = repo.Insert(title, year, plot, rating);
       if (outcome.IsSuccess()) {
           success = true;
       } else {
           const auto& error = outcome.GetError();
           if (error.GetExceptionName() == "ProvisionedThroughputExceededException") {
               retries++;
               std::this_thread::sleep_for(
                   std::chrono::milliseconds(static_cast<int>(pow(2, retries) * 100))
               );
           } else {
               std::cerr << "Error: " << error.GetMessage() << std::endl;
               break;
           }
       }
   }
   ```

### Logging

Configure AWS SDK logging:

```cpp
Aws::Utils::Logging::InitializeAWSLogging(
    Aws::MakeShared<Aws::Utils::Logging::DefaultLogSystem>(
        "RunMoviesDemoApp",
        Aws::Utils::Logging::LogLevel::Info,
        "aws_sdk_"
    )
);

// Use the repository...

Aws::Utils::Logging::ShutdownAWSLogging();
```

## Performance Optimization

### Connection Pooling

```cpp
Aws::Client::ClientConfiguration clientConfig;
clientConfig.region = Aws::Region::US_WEST_2;
clientConfig.maxConnections = 100;
clientConfig.connectTimeoutMs = 5000;
clientConfig.requestTimeoutMs = 10000;

auto dynamoClient = Aws::MakeShared<Aws::DynamoDB::DynamoDBClient>(
    "DynamoDBClient", clientConfig);
MovieRepository repo(dynamoClient);
```

### Batch Processing

For large datasets, use the batch write functionality with appropriate chunking:

```cpp
std::vector<Aws::Map<Aws::String, Aws::DynamoDB::Model::AttributeValue>> largeMovieList;
// ... populate large movie list ...

const size_t batchSize = 25; // DynamoDB batch write limit
for (size_t i = 0; i < largeMovieList.size(); i += batchSize) {
    std::vector<Aws::Map<Aws::String, Aws::DynamoDB::Model::AttributeValue>> batch;
    
    size_t end = std::min(i + batchSize, largeMovieList.size());
    for (size_t j = i; j < end; j++) {
        batch.push_back(largeMovieList[j]);
    }
    
    repo.WriteBatch(batch);
}
```

## Memory Management

The AWS SDK for C++ uses smart pointers extensively. When working with the SDK:

```cpp
// Use Aws::MakeShared instead of std::make_shared
auto client = Aws::MakeShared<Aws::DynamoDB::DynamoDBClient>(
    "DynamoDBClient", clientConfig);

// Use Aws::String instead of std::string for better compatibility
Aws::String tableName = "Movies";

// Use Aws::Vector instead of std::vector when appropriate
Aws::Vector<Aws::String> tableNames;
```

## API Reference

### Constructor

- `MovieRepository(std::shared_ptr<Aws::DynamoDB::DynamoDBClient> dynamoDbClient = nullptr, const Aws::String& tableName = "Movies")`: Initializes a new repository instance.

### Table Operations

- `bool Exists(const Aws::String& tableName)`: Checks if a table exists.
- `Aws::DynamoDB::Model::CreateTableOutcome CreateTable(const Aws::String& tableName)`: Creates a new table.
- `Aws::DynamoDB::Model::ListTablesOutcome ListTables()`: Lists all tables.
- `Aws::DynamoDB::Model::DeleteTableOutcome DeleteTable()`: Deletes the table.

### Item Operations

- `Aws::DynamoDB::Model::PutItemOutcome Insert(const Aws::String& title, int year, const Aws::String& plot, double rating)`: Adds a new movie.
- `Aws::DynamoDB::Model::GetItemOutcome Select(const Aws::String& title, int year)`: Retrieves a specific movie.
- `Aws::DynamoDB::Model::UpdateItemOutcome Update(const Aws::String& title, int year, const Aws::String& plot, double rating)`: Updates a movie's details.
- `Aws::DynamoDB::Model::DeleteItemOutcome Delete(const Aws::String& title, int year)`: Deletes a specific movie.

### Query Operations

- `Aws::DynamoDB::Model::QueryOutcome QueryMovies(int year)`: Finds movies from a specific year.
- `Aws::DynamoDB::Model::ScanOutcome ScanMovies(int firstYear, int secondYear)`: Finds movies within a year range.
- `Aws::DynamoDB::Model::BatchWriteItemOutcome WriteBatch(const std::vector<Aws::Map<Aws::String, Aws::DynamoDB::Model::AttributeValue>>& movies)`: Adds multiple movies in a batch.

## Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
