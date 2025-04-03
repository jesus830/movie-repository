
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Drive to the database
movies.insert(
    title="Drive", 
    year=2011, 
    plot="A mysterious Hollywood stuntman and mechanic moonlights as a getaway driver and finds himself in trouble when he helps out his neighbor.", 
    rating=7.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Drive", 
    year=2011
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    