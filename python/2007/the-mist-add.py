
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Mist to the database
movies.insert(
    title="The Mist", 
    year=2007, 
    plot="A freak storm unleashes a species of bloodthirsty creatures on a small town, where a small band of citizens hole up in a supermarket and fight for their lives.", 
    rating=7.2
)

# Confirm that the movie was added
movie = movies.select(
    title="The Mist", 
    year=2007
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    