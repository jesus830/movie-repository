
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Live Free or Die Hard to the database
movies.insert(
    title="Live Free or Die Hard", 
    year=2007, 
    plot="John McClane and a young hacker join forces to take down master cyber-terrorist Thomas Gabriel in Washington D.C.", 
    rating=7.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Live Free or Die Hard", 
    year=2007
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    