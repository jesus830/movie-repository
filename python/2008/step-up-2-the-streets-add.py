
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Step Up 2: The Streets to the database
movies.insert(
    title="Step Up 2: The Streets", 
    year=2008, 
    plot="Romantic sparks occur between two dance students from different backgrounds at the Maryland School of the Arts.", 
    rating=6.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Step Up 2: The Streets", 
    year=2008
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    