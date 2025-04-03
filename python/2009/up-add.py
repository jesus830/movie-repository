
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Up to the database
movies.insert(
    title="Up", 
    year=2009, 
    plot="Seventy-eight year old Carl Fredricksen travels to Paradise Falls in his home equipped with balloons, inadvertently taking a young stowaway.", 
    rating=8.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Up", 
    year=2009
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    