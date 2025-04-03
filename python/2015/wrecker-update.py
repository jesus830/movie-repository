
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Wrecker", 
    year=2015
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Wrecker", 
        year=2015, 
        plot="Best friends Emily and Lesley go on a road trip to the desert. When Emily decides to get off the highway and take a "short cut," they become the target of a relentless and psychotic trucker... See full summary »", 
        rating=3.5
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    