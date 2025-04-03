
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Fury to the database
movies.insert(
    title="Fury", 
    year=2014, 
    plot="A grizzled tank commander makes tough decisions as he and his crew fight their way across Germany in April, 1945.", 
    rating=7.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Fury", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    