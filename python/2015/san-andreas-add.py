
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add San Andreas to the database
movies.insert(
    title="San Andreas", 
    year=2015, 
    plot="In the aftermath of a massive earthquake in California, a rescue-chopper pilot makes a dangerous journey with his ex-wife across the state in order to rescue his daughter.", 
    rating=6.1
)

# Confirm that the movie was added
movie = movies.select(
    title="San Andreas", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    