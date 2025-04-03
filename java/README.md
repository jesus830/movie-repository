# Java DynamoDB Movie Database

## Overview

This Java implementation provides a robust and type-safe interface for managing a movie database using Amazon DynamoDB. The `MovieRepository` class offers a comprehensive set of operations for creating, reading, updating, and deleting movie data, along with powerful query and scan capabilities.

## Installation

### Prerequisites

- Java Development Kit (JDK) 8 or higher
- Maven or Gradle build tool
- AWS account with appropriate permissions
- AWS credentials configured locally

### Maven Dependencies

Add the following to your `pom.xml`:

```xml
<dependencies>
    <dependency>
        <groupId>com.amazonaws</groupId>
        <artifactId>aws-java-sdk-dynamodb</artifactId>
        <version>1.12.261</version>
    </dependency>
    <dependency>
        <groupId>org.slf4j</groupId>
        <artifactId>slf4j-api</artifactId>
        <version>1.7.36</version>
    </dependency>
    <dependency>
        <groupId>ch.qos.logback</groupId>
        <artifactId>logback-classic</artifactId>
        <version>1.2.11</version>
    </dependency>
</dependencies>
```

### Gradle Dependencies

Add the following to your `build.gradle`:

```groovy
dependencies {
    implementation 'com.amazonaws:aws-java-sdk-dynamodb:1.12.261'
    implementation 'org.slf4j:slf4j-api:1.7.36'
    implementation 'ch.qos.logback:logback-classic:1.2.11'
}
```

### AWS Configuration

1. Install the AWS CLI:
   ```bash
   brew install awscli  # macOS
   ```

2. Configure your AWS credentials:
   ```bash
   aws configure
   ```

## Usage

### Initializing the Repository

```java
import com.amazonaws.services.dynamodbv2.AmazonDynamoDB;
import com.amazonaws.services.dynamodbv2.AmazonDynamoDBClientBuilder;

// Initialize with default settings
MovieRepository repo = new MovieRepository();

// Or with a custom client and table name
AmazonDynamoDB client = AmazonDynamoDBClientBuilder.standard()
    .withRegion("us-west-2")
    .build();
MovieRepository repo = new MovieRepository(client, "CustomMoviesTable");
```

### Creating a Table

```java
if (!repo.exists("Movies")) {
    Table table = repo.createTable("Movies");
    System.out.println("Table created: " + table.getTableName());
}
```

### Adding Movies

```java
// Add a single movie
repo.insert(
    "The Matrix",
    1999,
    "A computer hacker learns about the true nature of reality.",
    new BigDecimal("8.7")
);

// Add multiple movies using batch write
List<Item> movies = new ArrayList<>();
movies.add(new Item()
    .withPrimaryKey("year", 1994, "title", "The Shawshank Redemption")
    .withMap("info", new HashMap<String, Object>() {{
        put("plot", "Two imprisoned men bond over a number of years.");
        put("rating", new BigDecimal("9.3"));
    }}));
movies.add(new Item()
    .withPrimaryKey("year", 1972, "title", "The Godfather")
    .withMap("info", new HashMap<String, Object>() {{
        put("plot", "The aging patriarch of an organized crime dynasty transfers control to his son.");
        put("rating", new BigDecimal("9.2"));
    }}));
repo.writeBatch(movies);
```

### Retrieving Movies

```java
// Get a specific movie by title and year
Item movie = repo.select("The Matrix", 1999);
System.out.println("Title: " + movie.getString("title"));
System.out.println("Year: " + movie.getNumber("year"));
Map<String, Object> info = movie.getMap("info");
System.out.println("Plot: " + info.get("plot"));
System.out.println("Rating: " + info.get("rating"));
```

### Updating Movies

```java
// Update a movie's plot and rating
Document updated = repo.update(
    "The Matrix",
    1999,
    "A computer programmer discovers a dystopian world is actually a simulation.",
    new BigDecimal("9.0")
);
System.out.println("Updated attributes: " + updated);
```

### Querying Movies

```java
// Find all movies released in 1999
List<Item> movies1999 = repo.queryMovies(1999);
System.out.println("Found " + movies1999.size() + " movies from 1999:");
for (Item movie : movies1999) {
    Map<String, Object> info = movie.getMap("info");
    System.out.printf("- %s: %s%n", 
        movie.getString("title"), 
        info.get("rating"));
}
```

### Scanning Movies

```java
// Find all movies released between 1990 and 1999
List<Item> ninetiesMovies = repo.scanMovies(1990, 1999);
System.out.println("Found " + ninetiesMovies.size() + " movies from the 90s:");
for (Item movie : ninetiesMovies) {
    Map<String, Object> info = movie.getMap("info");
    System.out.printf("- %s (%d): %s%n", 
        movie.getString("title"), 
        movie.getNumber("year"), 
        info.get("rating"));
}
```

### Deleting Movies

```java
// Delete a specific movie
repo.delete("The Matrix", 1999);
System.out.println("Movie deleted successfully");
```

### Deleting the Table

```java
// Delete the entire table when no longer needed
repo.deleteTable();
System.out.println("Table deleted successfully");
```

## Advanced Usage

### Custom DynamoDB Configuration

```java
AmazonDynamoDB client = AmazonDynamoDBClientBuilder.standard()
    .withRegion(Regions.US_WEST_2)
    .withClientConfiguration(new ClientConfiguration()
        .withConnectionTimeout(5000)
        .withRequestTimeout(10000)
        .withMaxErrorRetry(5))
    .build();
MovieRepository repo = new MovieRepository(client);
```

### Asynchronous Operations

While the MovieRepository methods are synchronous, you can wrap them in CompletableFuture for async operations:

```java
CompletableFuture.supplyAsync(() -> {
    try {
        return repo.queryMovies(1999);
    } catch (Exception e) {
        throw new CompletionException(e);
    }
}).thenAccept(movies -> {
    System.out.println("Found " + movies.size() + " movies");
}).exceptionally(e -> {
    System.err.println("Error: " + e.getMessage());
    return null;
});
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

2. **Table Already Exists**

   Handle the ResourceInUseException:
   ```java
   try {
       repo.createTable("Movies");
   } catch (ResourceInUseException e) {
       System.out.println("Table already exists");
   }
   ```

3. **Provisioned Throughput Exceeded**

   Implement exponential backoff:
   ```java
   int retries = 0;
   while (retries < 3) {
       try {
           repo.insert(title, year, plot, rating);
           break;
       } catch (ProvisionedThroughputExceededException e) {
           retries++;
           Thread.sleep((long) Math.pow(2, retries) * 100);
       }
   }
   ```

### Logging

Configure SLF4J logging with Logback. Create `logback.xml` in your resources directory:

```xml
<configuration>
    <appender name="CONSOLE" class="ch.qos.logback.core.ConsoleAppender">
        <encoder>
            <pattern>%d{HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n</pattern>
        </encoder>
    </appender>
    <root level="INFO">
        <appender-ref ref="CONSOLE" />
    </root>
</configuration>
```

## Performance Optimization

### Connection Pooling

```java
PooledHttpClientConnectionManager connectionManager = new PooledHttpClientConnectionManager();
connectionManager.setMaxTotal(100);
connectionManager.setDefaultMaxPerRoute(10);

ClientConfiguration clientConfig = new ClientConfiguration()
    .withConnectionTimeout(5000)
    .withRequestTimeout(10000)
    .withMaxConnections(100);

AmazonDynamoDB client = AmazonDynamoDBClientBuilder.standard()
    .withClientConfiguration(clientConfig)
    .build();
```

### Batch Processing

For large datasets, use the batch write functionality with appropriate chunking:

```java
List<Item> largeMovieList = // ... large list of movies ...
int batchSize = 25; // DynamoDB batch write limit
for (int i = 0; i < largeMovieList.size(); i += batchSize) {
    List<Item> batch = largeMovieList.subList(
        i, 
        Math.min(i + batchSize, largeMovieList.size())
    );
    repo.writeBatch(batch);
}
```

## API Reference

### Constructor Methods

- `MovieRepository()`: Default constructor
- `MovieRepository(AmazonDynamoDB client)`: Constructor with custom client
- `MovieRepository(AmazonDynamoDB client, String tableName)`: Constructor with custom client and table name

### Table Operations

- `boolean exists(String tableName)`: Checks if a table exists
- `Table createTable(String tableName)`: Creates a new table
- `List<String> listTables()`: Lists all tables
- `void deleteTable()`: Deletes the table

### Item Operations

- `void insert(String title, int year, String plot, BigDecimal rating)`: Adds a new movie
- `Item select(String title, int year)`: Retrieves a specific movie
- `Document update(String title, int year, String plot, BigDecimal rating)`: Updates a movie's details
- `void delete(String title, int year)`: Deletes a specific movie

### Query Operations

- `List<Item> queryMovies(int year)`: Finds movies from a specific year
- `List<Item> scanMovies(int firstYear, int secondYear)`: Finds movies within a year range
- `void writeBatch(List<Item> movies)`: Adds multiple movies in a batch

## Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
