
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Collateral Beauty", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Collateral Beauty", 
        year=2016, 
        plot="Retreating from life after a tragedy, a man questions the universe by writing to Love, Time and Death. Receiving unexpected answers, he begins to see how these things interlock and how even loss can reveal moments of meaning and beauty.", 
        rating=6.8
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    