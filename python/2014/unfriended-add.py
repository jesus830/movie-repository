
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Unfriended to the database
movies.insert(
    title="Unfriended", 
    year=2014, 
    plot="A group of online chat room friends find themselves haunted by a mysterious, supernatural force using the account of their dead friend.", 
    rating=5.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Unfriended", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    