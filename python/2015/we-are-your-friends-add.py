
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add We Are Your Friends to the database
movies.insert(
    title="We Are Your Friends", 
    year=2015, 
    plot="Caught between a forbidden romance and the expectations of his friends, aspiring DJ Cole Carter attempts to find the path in life that leads to fame and fortune.", 
    rating=6.2
)

# Confirm that the movie was added
movie = movies.select(
    title="We Are Your Friends", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    