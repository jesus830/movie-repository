
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Friday the 13th to the database
movies.insert(
    title="Friday the 13th", 
    year=2009, 
    plot="A group of young adults discover a boarded up Camp Crystal Lake, where they soon encounter Jason Voorhees and his deadly intentions.", 
    rating=5.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Friday the 13th", 
    year=2009
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    