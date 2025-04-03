
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Café Society to the database
movies.insert(
    title="Café Society", 
    year=2016, 
    plot="In the 1930s, a Bronx native moves to Hollywood and falls in love with a young woman who is seeing a married man.", 
    rating=6.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Café Society", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    