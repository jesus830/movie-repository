
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The 9th Life of Louis Drax to the database
movies.insert(
    title="The 9th Life of Louis Drax", 
    year=2016, 
    plot="A psychologist who begins working with a young boy who has suffered a near-fatal fall finds himself drawn into a mystery that tests the boundaries of fantasy and reality.", 
    rating=6.3
)

# Confirm that the movie was added
movie = movies.select(
    title="The 9th Life of Louis Drax", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    