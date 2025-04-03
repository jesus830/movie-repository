# Python DynamoDB Movie Database

## Overview

This Python implementation provides a comprehensive interface for working with a movie database stored in Amazon DynamoDB. The `MovieRepository` class encapsulates all the functionality needed to create, read, update, and delete movie data, as well as perform queries and scans across the database.

## Installation

### Prerequisites

- Python 3.6 or higher
- AWS account with appropriate permissions
- AWS credentials configured locally

### Setting Up

1. Install the required dependencies:

```bash
pip install boto3 requests
```

2. Configure your AWS credentials:

```bash
aws configure
```

Enter your AWS Access Key ID, Secret Access Key, default region, and output format when prompted.

3. Clone this repository:

```bash
git clone https://github.com/yourusername/amazon-q-customization-demo-python.git
cd amazon-q-customization-demo-python/python
```

## Usage

### Initializing the Repository

```python
from movies import MovieRepository

# Initialize with default settings (uses "Movies" table)
repo = MovieRepository()

# Or specify a custom table name
repo = MovieRepository(table_name="CustomMoviesTable")

# Or provide your own DynamoDB resource
import boto3
dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
repo = MovieRepository(dyn_resource=dynamodb, table_name="CustomMoviesTable")
```

### Creating a Table

```python
# Create a new table if it doesn't exist
if not repo.exists("Movies"):
    repo.create_table("Movies")
```

### Adding Movies

```python
# Add a single movie
repo.insert(
    title="The Matrix",
    year=1999,
    plot="A computer hacker learns about the true nature of reality.",
    rating=8.7
)

# Add multiple movies using batch write
movies = [
    {
        "year": 1994,
        "title": "The Shawshank Redemption",
        "info": {
            "plot": "Two imprisoned men bond over a number of years.",
            "rating": 9.3
        }
    },
    {
        "year": 1972,
        "title": "The Godfather",
        "info": {
            "plot": "The aging patriarch of an organized crime dynasty transfers control to his son.",
            "rating": 9.2
        }
    }
]
repo.write_batch(movies)
```

### Retrieving Movies

```python
# Get a specific movie by title and year
movie = repo.select("The Matrix", 1999)
print(f"Title: {movie['title']}")
print(f"Year: {movie['year']}")
print(f"Plot: {movie['info']['plot']}")
print(f"Rating: {movie['info']['rating']}")
```

### Updating Movies

```python
# Update a movie's plot and rating
updated = repo.update(
    title="The Matrix",
    year=1999,
    plot="A computer programmer discovers a dystopian world is actually a simulation.",
    rating=9.0
)
print("Updated attributes:", updated)
```

### Querying Movies

```python
# Find all movies released in 1999
movies_1999 = repo.query_movies(1999)
print(f"Found {len(movies_1999)} movies from 1999:")
for movie in movies_1999:
    print(f"- {movie['title']}: {movie['info']['rating']}")
```

### Scanning Movies

```python
# Find all movies released between 1990 and 1999
nineties_movies = repo.scan_movies({"first": 1990, "second": 1999})
print(f"Found {len(nineties_movies)} movies from the 90s:")
for movie in nineties_movies:
    print(f"- {movie['title']} ({movie['year']}): {movie['info']['rating']}")
```

### Deleting Movies

```python
# Delete a specific movie
repo.delete("The Matrix", 1999)
print("Movie deleted successfully")
```

### Deleting the Table

```python
# Delete the entire table when no longer needed
repo.delete_table()
print("Table deleted successfully")
```

## Advanced Usage

### Listing Tables

```python
# List all DynamoDB tables in your account
tables = repo.list_tables()
print("Available tables:", tables)
```

### Error Handling

The `MovieRepository` class includes comprehensive error handling. All methods will raise appropriate exceptions with detailed error messages if operations fail.

```python
try:
    movie = repo.select("Non-existent Movie", 2099)
except Exception as e:
    print(f"Error retrieving movie: {e}")
```

## Troubleshooting

### Common Issues

1. **Authentication Errors**

   If you see errors related to authentication, ensure your AWS credentials are properly configured:

   ```bash
   aws configure
   ```

2. **Table Does Not Exist**

   If operations fail because the table doesn't exist, create it first:

   ```python
   if not repo.exists("Movies"):
       repo.create_table("Movies")
   ```

3. **Throttling Exceptions**

   If you're experiencing throttling exceptions, you might be exceeding your provisioned throughput:

   ```python
   # Increase the provisioned throughput when creating the table
   table = repo.dyn_resource.create_table(
       # ... other parameters ...
       ProvisionedThroughput={
           "ReadCapacityUnits": 25,  # Increased from default 10
           "WriteCapacityUnits": 25  # Increased from default 10
       }
   )
   ```

4. **Region Issues**

   Ensure you're operating in the correct AWS region:

   ```python
   import boto3
   dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
   repo = MovieRepository(dyn_resource=dynamodb)
   ```

### Logging

The `MovieRepository` class uses Python's built-in logging module. To see more detailed logs:

```python
import logging
logging.basicConfig(level=logging.INFO)
```

For even more verbose logging:

```python
logging.basicConfig(level=logging.DEBUG)
```

## Performance Optimization

### Batch Operations

For large datasets, use batch operations instead of individual calls:

```python
# Much faster than individual inserts for large datasets
repo.write_batch(large_movie_list)
```

### Pagination

When querying or scanning for large result sets, be aware that the results might be paginated:

```python
# The scan_movies method already handles pagination internally
all_movies = repo.scan_movies({"first": 1900, "second": 2023})
```

## API Reference

### Constructor

- `MovieRepository(dyn_resource=None, table_name=None)`: Initializes a new repository instance.

### Table Operations

- `exists(table_name)`: Checks if a table exists.
- `create_table(table_name)`: Creates a new table.
- `list_tables()`: Lists all tables.
- `delete_table()`: Deletes the table.

### Item Operations

- `insert(title, year, plot, rating)`: Adds a new movie.
- `select(title, year)`: Retrieves a specific movie.
- `update(title, year, plot, rating)`: Updates a movie's details.
- `delete(title, year)`: Deletes a specific movie.

### Query Operations

- `query_movies(year)`: Finds movies from a specific year.
- `scan_movies(year_range)`: Finds movies within a year range.
- `write_batch(movies)`: Adds multiple movies in a batch.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
