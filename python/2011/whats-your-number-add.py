
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add What's Your Number? to the database
movies.insert(
    title="What's Your Number?", 
    year=2011, 
    plot="A woman looks back at the past nineteen men she's had relationships with in her life and wonders if one of them might be her one true love.", 
    rating=6.1
)

# Confirm that the movie was added
movie = movies.select(
    title="What's Your Number?", 
    year=2011
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    