
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add I.T. to the database
movies.insert(
    title="I.T.", 
    year=2016, 
    plot="A self-proclaimed millionaire, has his life turned upside down after firing his I.T. consultant.", 
    rating=5.4
)

# Confirm that the movie was added
movie = movies.select(
    title="I.T.", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    