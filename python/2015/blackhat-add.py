
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Blackhat to the database
movies.insert(
    title="Blackhat", 
    year=2015, 
    plot="A furloughed convict and his American and Chinese partners hunt a high-level cybercrime network from Chicago to Los Angeles to Hong Kong to Jakarta.", 
    rating=5.4
)

# Confirm that the movie was added
movie = movies.select(
    title="Blackhat", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    