
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Collateral Beauty to the database
movies.insert(
    title="Collateral Beauty", 
    year=2016, 
    plot="Retreating from life after a tragedy, a man questions the universe by writing to Love, Time and Death. Receiving unexpected answers, he begins to see how these things interlock and how even loss can reveal moments of meaning and beauty.", 
    rating=6.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Collateral Beauty", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    