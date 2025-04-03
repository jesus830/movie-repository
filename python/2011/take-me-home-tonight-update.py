
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Take Me Home Tonight", 
    year=2011
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Take Me Home Tonight", 
        year=2011, 
        plot="Four years after graduation, an awkward high school genius uses his sister's boyfriend's Labor Day party as the perfect opportunity to make his move on his high school crush.", 
        rating=6.3
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    