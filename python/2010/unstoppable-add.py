
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Unstoppable to the database
movies.insert(
    title="Unstoppable", 
    year=2010, 
    plot="With an unmanned, half-mile-long freight train barreling toward a city, a veteran engineer and a young conductor race against the clock to prevent a catastrophe.", 
    rating=6.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Unstoppable", 
    year=2010
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    