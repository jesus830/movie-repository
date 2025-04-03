
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Free Fire", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Free Fire", 
        year=2016, 
        plot="Set in Boston in 1978, a meeting in a deserted warehouse between two gangs turns into a shootout and a game of survival.", 
        rating=7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    