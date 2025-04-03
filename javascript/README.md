# JavaScript DynamoDB Movie Database

## Overview

This JavaScript implementation provides a modern, Promise-based interface for managing a movie database using Amazon DynamoDB. The `MovieRepository` class encapsulates all the functionality needed to create, read, update, and delete movie data, as well as perform queries and scans across the database.

## Installation

### Prerequisites

- Node.js 12.x or higher
- npm or yarn package manager
- AWS account with appropriate permissions
- AWS credentials configured locally

### Setting Up

1. Install the required dependencies:

```bash
npm install aws-sdk
# or
yarn add aws-sdk
```

2. Configure your AWS credentials:

```bash
npm install -g aws-cli
aws configure
```

Enter your AWS Access Key ID, Secret Access Key, default region, and output format when prompted.

3. Clone this repository:

```bash
git clone https://github.com/yourusername/amazon-q-customization-demo-python.git
cd amazon-q-customization-demo-python/javascript
```

4. Create a `.env` file for environment variables (optional):

```
AWS_REGION=us-west-2
AWS_PROFILE=default
MOVIES_TABLE_NAME=Movies
```

## Usage

### Initializing the Repository

```javascript
const AWS = require('aws-sdk');
const MovieRepository = require('./MovieRepository');

// Initialize with default settings (uses "Movies" table)
const repo = new MovieRepository();

// Or specify a custom table name
const repo = new MovieRepository(null, 'CustomMoviesTable');

// Or provide your own DynamoDB client
const dynamoDB = new AWS.DynamoDB.DocumentClient({
  region: 'us-west-2',
  apiVersion: '2012-08-10'
});
const repo = new MovieRepository(dynamoDB, 'CustomMoviesTable');
```

### Creating a Table

```javascript
// Create a new table if it doesn't exist
const tableExists = await repo.exists('Movies');
if (!tableExists) {
  const table = await repo.createTable('Movies');
  console.log(`Table created: ${table.TableDescription.TableName}`);
}
```

### Adding Movies

```javascript
// Add a single movie
await repo.insert(
  'The Matrix',
  1999,
  'A computer hacker learns about the true nature of reality.',
  8.7
);

// Add multiple movies using batch write
const movies = [
  {
    year: 1994,
    title: 'The Shawshank Redemption',
    info: {
      plot: 'Two imprisoned men bond over a number of years.',
      rating: 9.3
    }
  },
  {
    year: 1972,
    title: 'The Godfather',
    info: {
      plot: 'The aging patriarch of an organized crime dynasty transfers control to his son.',
      rating: 9.2
    }
  }
];
await repo.writeBatch(movies);
```

### Retrieving Movies

```javascript
// Get a specific movie by title and year
const movie = await repo.select('The Matrix', 1999);
console.log(`Title: ${movie.title}`);
console.log(`Year: ${movie.year}`);
console.log(`Plot: ${movie.info.plot}`);
console.log(`Rating: ${movie.info.rating}`);
```

### Updating Movies

```javascript
// Update a movie's plot and rating
const updated = await repo.update(
  'The Matrix',
  1999,
  'A computer programmer discovers a dystopian world is actually a simulation.',
  9.0
);
console.log('Updated attributes:', updated);
```

### Querying Movies

```javascript
// Find all movies released in 1999
const movies1999 = await repo.queryMovies(1999);
console.log(`Found ${movies1999.length} movies from 1999:`);
movies1999.forEach(movie => {
  console.log(`- ${movie.title}: ${movie.info.rating}`);
});
```

### Scanning Movies

```javascript
// Find all movies released between 1990 and 1999
const ninetiesMovies = await repo.scanMovies({ first: 1990, second: 1999 });
console.log(`Found ${ninetiesMovies.length} movies from the 90s:`);
ninetiesMovies.forEach(movie => {
  console.log(`- ${movie.title} (${movie.year}): ${movie.info.rating}`);
});
```

### Deleting Movies

```javascript
// Delete a specific movie
await repo.delete('The Matrix', 1999);
console.log('Movie deleted successfully');
```

### Deleting the Table

```javascript
// Delete the entire table when no longer needed
await repo.deleteTable();
console.log('Table deleted successfully');
```

## Advanced Usage

### Listing Tables

```javascript
// List all DynamoDB tables in your account
const tables = await repo.listTables();
console.log('Available tables:', tables);
```

### Using with Express.js

```javascript
const express = require('express');
const MovieRepository = require('./MovieRepository');

const app = express();
app.use(express.json());
const repo = new MovieRepository();

// Get a movie
app.get('/movies/:year/:title', async (req, res) => {
  try {
    const { year, title } = req.params;
    const movie = await repo.select(title, parseInt(year, 10));
    if (!movie) {
      return res.status(404).json({ error: 'Movie not found' });
    }
    res.json(movie);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Add a movie
app.post('/movies', async (req, res) => {
  try {
    const { title, year, plot, rating } = req.body;
    await repo.insert(title, year, plot, rating);
    res.status(201).json({ message: 'Movie created successfully' });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.listen(3000, () => {
  console.log('Server running on port 3000');
});
```

### Using with AWS Lambda

```javascript
const MovieRepository = require('./MovieRepository');
const repo = new MovieRepository();

exports.handler = async (event) => {
  try {
    const { httpMethod, pathParameters, body } = event;
    
    if (httpMethod === 'GET' && pathParameters) {
      const { year, title } = pathParameters;
      const movie = await repo.select(title, parseInt(year, 10));
      return {
        statusCode: 200,
        body: JSON.stringify(movie)
      };
    }
    
    if (httpMethod === 'POST') {
      const { title, year, plot, rating } = JSON.parse(body);
      await repo.insert(title, year, plot, rating);
      return {
        statusCode: 201,
        body: JSON.stringify({ message: 'Movie created successfully' })
      };
    }
    
    return {
      statusCode: 400,
      body: JSON.stringify({ message: 'Invalid request' })
    };
  } catch (err) {
    return {
      statusCode: 500,
      body: JSON.stringify({ error: err.message })
    };
  }
};
```

## Error Handling

The `MovieRepository` class includes comprehensive error handling. All methods will throw appropriate exceptions with detailed error messages if operations fail.

```javascript
try {
  const movie = await repo.select('Non-existent Movie', 2099);
  console.log(movie);
} catch (err) {
  console.error(`Error retrieving movie: ${err.message}`);
}
```

## Troubleshooting

### Common Issues

1. **Authentication Errors**

   If you see errors related to authentication, ensure your AWS credentials are properly configured:

   ```bash
   aws configure
   ```

   Or set them in environment variables:

   ```bash
   export AWS_ACCESS_KEY_ID=YOUR_ACCESS_KEY
   export AWS_SECRET_ACCESS_KEY=YOUR_SECRET_KEY
   ```

2. **Table Does Not Exist**

   If operations fail because the table doesn't exist, create it first:

   ```javascript
   if (!(await repo.exists('Movies'))) {
     await repo.createTable('Movies');
   }
   ```

3. **Throttling Exceptions**

   If you're experiencing throttling exceptions, implement exponential backoff:

   ```javascript
   const backoff = async (fn, retries = 3) => {
     let lastError;
     for (let i = 0; i < retries; i++) {
       try {
         return await fn();
       } catch (err) {
         if (err.code === 'ProvisionedThroughputExceededException') {
           lastError = err;
           const delay = Math.pow(2, i) * 100;
           await new Promise(resolve => setTimeout(resolve, delay));
         } else {
           throw err;
         }
       }
     }
     throw lastError;
   };

   await backoff(() => repo.insert(title, year, plot, rating));
   ```

4. **Region Issues**

   Ensure you're operating in the correct AWS region:

   ```javascript
   const dynamoDB = new AWS.DynamoDB.DocumentClient({
     region: 'us-east-1'
   });
   const repo = new MovieRepository(dynamoDB);
   ```

### Logging

The `MovieRepository` class uses a simple logger module. To customize logging:

```javascript
// Create a custom logger
const customLogger = {
  error: (message) => console.error(`[ERROR] ${new Date().toISOString()} - ${message}`),
  info: (message) => console.info(`[INFO] ${new Date().toISOString()} - ${message}`),
  warn: (message) => console.warn(`[WARN] ${new Date().toISOString()} - ${message}`),
  debug: (message) => console.debug(`[DEBUG] ${new Date().toISOString()} - ${message}`)
};

// Replace the logger in the module
const logger = require('./logger');
Object.assign(logger, customLogger);
```

## Performance Optimization

### Connection Pooling

AWS SDK for JavaScript automatically manages connection pooling, but you can configure it:

```javascript
const dynamoDB = new AWS.DynamoDB.DocumentClient({
  httpOptions: {
    agent: new https.Agent({
      keepAlive: true,
      maxSockets: 50,
      rejectUnauthorized: true
    })
  }
});
const repo = new MovieRepository(dynamoDB);
```

### Batch Operations

For large datasets, use batch operations instead of individual calls:

```javascript
// Much faster than individual inserts for large datasets
const largeMovieList = [/* many movies */];
const batchSize = 25; // DynamoDB batch write limit

for (let i = 0; i < largeMovieList.length; i += batchSize) {
  const batch = largeMovieList.slice(i, i + batchSize);
  await repo.writeBatch(batch);
}
```

## API Reference

### Constructor

- `MovieRepository(docClient = null, tableName = 'Movies')`: Initializes a new repository instance.

### Table Operations

- `async exists(tableName)`: Checks if a table exists.
- `async createTable(tableName)`: Creates a new table.
- `async listTables()`: Lists all tables.
- `async deleteTable()`: Deletes the table.

### Item Operations

- `async insert(title, year, plot, rating)`: Adds a new movie.
- `async select(title, year)`: Retrieves a specific movie.
- `async update(title, year, plot, rating)`: Updates a movie's details.
- `async delete(title, year)`: Deletes a specific movie.

### Query Operations

- `async queryMovies(year)`: Finds movies from a specific year.
- `async scanMovies(yearRange)`: Finds movies within a year range.
- `async writeBatch(movies)`: Adds multiple movies in a batch.

## Testing

Example of testing with Jest:

```javascript
const MovieRepository = require('./MovieRepository');

// Mock AWS SDK
jest.mock('aws-sdk', () => {
  const mockDocumentClient = {
    put: jest.fn().mockReturnThis(),
    get: jest.fn().mockReturnThis(),
    update: jest.fn().mockReturnThis(),
    delete: jest.fn().mockReturnThis(),
    query: jest.fn().mockReturnThis(),
    scan: jest.fn().mockReturnThis(),
    batchWrite: jest.fn().mockReturnThis(),
    promise: jest.fn()
  };
  
  return {
    DynamoDB: {
      DocumentClient: jest.fn(() => mockDocumentClient),
      waitFor: jest.fn().mockReturnThis(),
      promise: jest.fn()
    }
  };
});

describe('MovieRepository', () => {
  let repo;
  let mockDocClient;
  
  beforeEach(() => {
    mockDocClient = new AWS.DynamoDB.DocumentClient();
    repo = new MovieRepository(mockDocClient);
  });
  
  test('insert should call put with correct parameters', async () => {
    mockDocClient.promise.mockResolvedValueOnce({});
    
    await repo.insert('Test Movie', 2023, 'Test plot', 8.5);
    
    expect(mockDocClient.put).toHaveBeenCalledWith({
      TableName: 'Movies',
      Item: {
        year: 2023,
        title: 'Test Movie',
        info: {
          plot: 'Test plot',
          rating: 8.5
        }
      }
    });
  });
});
```

## Contributing

We welcome contributions! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
