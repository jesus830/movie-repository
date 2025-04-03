
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Strangers to the database
movies.insert(
    title="The Strangers", 
    year=2008, 
    plot="A young couple staying in an isolated vacation home are terrorized by three unknown assailants.", 
    rating=6.2
)

# Confirm that the movie was added
movie = movies.select(
    title="The Strangers", 
    year=2008
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    