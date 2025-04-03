
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Host to the database
movies.insert(
    title="The Host", 
    year=2006, 
    plot="A monster emerges from Seoul's Han River and focuses its attention on attacking people. One victim's loving family does what it can to rescue her from its clutches.", 
    rating=7
)

# Confirm that the movie was added
movie = movies.select(
    title="The Host", 
    year=2006
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    