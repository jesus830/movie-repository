
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Goosebumps to the database
movies.insert(
    title="Goosebumps", 
    year=2015, 
    plot="A teenager teams up with the daughter of young adult horror author R. L. Stine after the writer's imaginary demons are set free on the town of Madison, Delaware.", 
    rating=6.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Goosebumps", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    