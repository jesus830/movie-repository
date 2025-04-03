
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Teenage Mutant Ninja Turtles to the database
movies.insert(
    title="Teenage Mutant Ninja Turtles", 
    year=2014, 
    plot="When a kingpin threatens New York City, a group of mutated turtle warriors must emerge from the shadows to protect their home.", 
    rating=5.9
)

# Confirm that the movie was added
movie = movies.select(
    title="Teenage Mutant Ninja Turtles", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    