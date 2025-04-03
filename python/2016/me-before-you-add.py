
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Me Before You to the database
movies.insert(
    title="Me Before You", 
    year=2016, 
    plot="A girl in a small town forms an unlikely bond with a recently-paralyzed man she's taking care of.", 
    rating=7.4
)

# Confirm that the movie was added
movie = movies.select(
    title="Me Before You", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    