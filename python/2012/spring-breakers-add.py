
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Spring Breakers to the database
movies.insert(
    title="Spring Breakers", 
    year=2012, 
    plot="Four college girls hold up a restaurant in order to fund their spring break vacation. While partying, drinking, and taking drugs, they are arrested, only to be bailed out by a drug and arms dealer.", 
    rating=5.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Spring Breakers", 
    year=2012
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    