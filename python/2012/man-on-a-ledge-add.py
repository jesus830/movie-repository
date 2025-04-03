
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Man on a Ledge to the database
movies.insert(
    title="Man on a Ledge", 
    year=2012, 
    plot="As a police psychologist works to talk down an ex-con who is threatening to jump from a Manhattan hotel rooftop, the biggest diamond heist ever committed is in motion.", 
    rating=6.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Man on a Ledge", 
    year=2012
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    