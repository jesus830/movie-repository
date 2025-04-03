
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Take Me Home Tonight to the database
movies.insert(
    title="Take Me Home Tonight", 
    year=2011, 
    plot="Four years after graduation, an awkward high school genius uses his sister's boyfriend's Labor Day party as the perfect opportunity to make his move on his high school crush.", 
    rating=6.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Take Me Home Tonight", 
    year=2011
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    