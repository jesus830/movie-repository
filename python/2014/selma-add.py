
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Selma to the database
movies.insert(
    title="Selma", 
    year=2014, 
    plot="A chronicle of Martin Luther King's campaign to secure equal voting rights via an epic march from Selma to Montgomery, Alabama in 1965.", 
    rating=7.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Selma", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    