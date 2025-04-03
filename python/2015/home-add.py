
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Home to the database
movies.insert(
    title="Home", 
    year=2015, 
    plot="An alien on the run from his own people makes friends with a girl. He tries to help her on her quest, but can be an interference.", 
    rating=6.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Home", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    