# TypeScript DynamoDB Movie Database

## Overview

This TypeScript implementation provides a strongly-typed, Promise-based interface for managing a movie database using Amazon DynamoDB. The `MovieRepository` class encapsulates all the functionality needed to create, read, update, and delete movie data, as well as perform queries and scans across the database.

## Installation

### Prerequisites

- Node.js 14.x or higher
- npm or yarn package manager
- TypeScript 4.x or higher
- AWS account with appropriate permissions
- AWS credentials configured locally

### Setting Up

1. Install the required dependencies:

```bash
npm install aws-sdk typescript ts-node @types/node
# or
yarn add aws-sdk typescript ts-node @types/node
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
cd amazon-q-customization-demo-python/typescript
```

4. Create a `tsconfig.json` file:

```json
{
  "compilerOptions": {
    "target": "ES2018",
    "module": "commonjs",
    "lib": ["es2018", "dom"],
    "declaration": true,
    "strict": true,
    "noImplicitAny": true,
    "strictNullChecks": true,
    "noImplicitThis": true,
    "alwaysStrict": true,
    "noUnusedLocals": false,
    "noUnusedParameters": false,
    "noImplicitReturns": true,
    "noFallthroughCasesInSwitch": false,
    "inlineSourceMap": true,
    "inlineSources": true,
    "experimentalDecorators": true,
    "strictPropertyInitialization": false,
    "outDir": "./dist",
    "rootDir": "./src"
  },
  "exclude": ["node_modules", "dist"]
}
```

5. Create a `.env` file for environment variables (optional):

```
AWS_REGION=us-west-2
AWS_PROFILE=default
MOVIES_TABLE_NAME=Movies
```

## Usage

### Initializing the Repository

```typescript
import { DocumentClient } from 'aws-sdk/clients/dynamodb';
import * as AWS from 'aws-sdk';
import { MovieRepository } from './MovieRepository';

// Initialize with default settings (uses "Movies" table)
const repo = new MovieRepository();

// Or specify a custom table name
const repo = new MovieRepository(undefined, 'CustomMoviesTable');

// Or provide your own DynamoDB client
const docClient = new AWS.DynamoDB.DocumentClient({
  region: 'us-west-2',
  apiVersion: '2012-08-10'
});
const repo = new MovieRepository(docClient, 'CustomMoviesTable');
```

### Creating a Table

```typescript
// Create a new table if it doesn't exist
const tableExists = await repo.exists('Movies');
if (!tableExists) {
  const table = await repo.createTable('Movies');
  console.log(`Table created: ${table.TableDescription?.TableName}`);
}
```

### Adding Movies

```typescript
// Add a single movie
await repo.insert(
  'The Matrix',
  1999,
  'A computer hacker learns about the true nature of reality.',
  8.7
);

// Add multiple movies using batch write
interface MovieInfo {
  plot: string;
  rating: number;
}

interface Movie {
  year: number;
  title: string;
  info: MovieInfo;
}

const movies: Movie[] = [
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

```typescript
// Get a specific movie by title and year
const movie = await repo.select('The Matrix', 1999);
if (movie) {
  console.log(`Title: ${movie.title}`);
  console.log(`Year: ${movie.year}`);
  console.log(`Plot: ${movie.info.plot}`);
  console.log(`Rating: ${movie.info.rating}`);
}
```

### Updating Movies

```typescript
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

```typescript
// Find all movies released in 1999
const movies1999 = await repo.queryMovies(1999);
console.log(`Found ${movies1999.length} movies from 1999:`);
movies1999.forEach(movie => {
  console.log(`- ${movie.title}: ${movie.info.rating}`);
});
```

### Scanning Movies

```typescript
// Find all movies released between 1990 and 1999
const ninetiesMovies = await repo.scanMovies({ first: 1990, second: 1999 });
console.log(`Found ${ninetiesMovies.length} movies from the 90s:`);
ninetiesMovies.forEach(movie => {
  console.log(`- ${movie.title} (${movie.year}): ${movie.info.rating}`);
});
```

### Deleting Movies

```typescript
// Delete a specific movie
await repo.delete('The Matrix', 1999);
console.log('Movie deleted successfully');
```

### Deleting the Table

```typescript
// Delete the entire table when no longer needed
await repo.deleteTable();
console.log('Table deleted successfully');
```

## Advanced Usage

### Listing Tables

```typescript
// List all DynamoDB tables in your account
const tables = await repo.listTables();
console.log('Available tables:', tables);
```

### Using with Express.js

```typescript
import express from 'express';
import { MovieRepository } from './MovieRepository';

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
interface MovieRequest {
  title: string;
  year: number;
  plot: string;
  rating: number;
}

app.post('/movies', async (req, res) => {
  try {
    const { title, year, plot, rating } = req.body as MovieRequest;
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

```typescript
import { APIGatewayProxyEvent, APIGatewayProxyResult } from 'aws-lambda';
import { MovieRepository } from './MovieRepository';

const repo = new MovieRepository();

interface MovieRequest {
  title: string;
  year: number;
  plot: string;
  rating: number;
}

export const handler = async (event: APIGatewayProxyEvent): Promise<APIGatewayProxyResult> => {
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
    
    if (httpMethod === 'POST' && body) {
      const { title, year, plot, rating } = JSON.parse(body) as MovieRequest;
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

The `MovieRepository` class includes comprehensive error handling with TypeScript's strong typing. All methods will throw appropriate exceptions with detailed error messages if operations fail.

```typescript
try {
  const movie = await repo.select('Non-existent Movie', 2099);
  if (movie) {
    console.log(movie);
  } else {
    console.log('Movie not found');
  }
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

   ```typescript
   if (!(await repo.exists('Movies'))) {
     await repo.createTable('Movies');
   }
   ```

3. **Throttling Exceptions**

   If you're experiencing throttling exceptions, implement exponential backoff:

   ```typescript
   const backoff = async <T>(fn: () => Promise<T>, retries = 3): Promise<T> => {
     let lastError: Error;
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

   ```typescript
   const docClient = new AWS.DynamoDB.DocumentClient({
     region: 'us-east-1'
   });
   const repo = new MovieRepository(docClient);
   ```

### Logging

Configure logging with a custom logger:

```typescript
// Create a custom logger
interface Logger {
  error(message: string): void;
  info(message: string): void;
  warn(message: string): void;
  debug(message: string): void;
}

const logger: Logger = {
  error: (message: string) => console.error(`[ERROR] ${new Date().toISOString()} - ${message}`),
  info: (message: string) => console.info(`[INFO] ${new Date().toISOString()} - ${message}`),
  warn: (message: string) => console.warn(`[WARN] ${new Date().toISOString()} - ${message}`),
  debug: (message: string) => console.debug(`[DEBUG] ${new Date().toISOString()} - ${message}`)
};

// Use the logger in your application
logger.info('Application started');
```

## Performance Optimization

### Connection Pooling

AWS SDK for JavaScript/TypeScript automatically manages connection pooling, but you can configure it:

```typescript
import * as https from 'https';

const docClient = new AWS.DynamoDB.DocumentClient({
  httpOptions: {
    agent: new https.Agent({
      keepAlive: true,
      maxSockets: 50,
      rejectUnauthorized: true
    })
  }
});
const repo = new MovieRepository(docClient);
```

### Batch Operations

For large datasets, use batch operations instead of individual calls:

```typescript
// Much faster than individual inserts for large datasets
const largeMovieList: Movie[] = [/* many movies */];
const batchSize = 25; // DynamoDB batch write limit

for (let i = 0; i < largeMovieList.length; i += batchSize) {
  const batch = largeMovieList.slice(i, i + batchSize);
  await repo.writeBatch(batch);
}
```

## API Reference

### Interfaces

```typescript
interface MovieInfo {
  plot: string;
  rating: number;
}

interface Movie {
  year: number;
  title: string;
  info: MovieInfo;
}

interface YearRange {
  first: number;
  second: number;
}
```

### Constructor

- `constructor(docClient?: DocumentClient, tableName: string = 'Movies')`: Initializes a new repository instance.

### Table Operations

- `async exists(tableName: string): Promise<boolean>`: Checks if a table exists.
- `async createTable(tableName: string): Promise<AWS.DynamoDB.CreateTableOutput>`: Creates a new table.
- `async listTables(): Promise<string[]>`: Lists all tables.
- `async deleteTable(): Promise<void>`: Deletes the table.

### Item Operations

- `async insert(title: string, year: number, plot: string, rating: number): Promise<void>`: Adds a new movie.
- `async select(title: string, year: number): Promise<Movie | undefined>`: Retrieves a specific movie.
- `async update(title: string, year: number, plot: string, rating: number): Promise<DocumentClient.AttributeMap>`: Updates a movie's details.
- `async delete(title: string, year: number): Promise<void>`: Deletes a specific movie.

### Query Operations

- `async queryMovies(year: number): Promise<Movie[]>`: Finds movies from a specific year.
- `async scanMovies(yearRange: YearRange): Promise<Movie[]>`: Finds movies within a year range.
- `async writeBatch(movies: Movie[]): Promise<void>`: Adds multiple movies in a batch.

## Testing

Example of testing with Jest:

```typescript
import { MovieRepository } from './MovieRepository';
import { DocumentClient } from 'aws-sdk/clients/dynamodb';

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
      DocumentClient: jest.fn(() => mockDocumentClient)
    }
  };
});

describe('MovieRepository', () => {
  let repo: MovieRepository;
  let mockDocClient: DocumentClient;
  
  beforeEach(() => {
    mockDocClient = new DocumentClient();
    repo = new MovieRepository(mockDocClient);
  });
  
  test('insert should call put with correct parameters', async () => {
    (mockDocClient.put().promise as jest.Mock).mockResolvedValueOnce({});
    
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
