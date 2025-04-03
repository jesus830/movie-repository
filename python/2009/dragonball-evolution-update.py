
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Dragonball Evolution", 
    year=2009
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Dragonball Evolution", 
        year=2009, 
        plot="The young warrior Son Goku sets out on a quest, racing against time and the vengeful King Piccolo, to collect a set of seven magical orbs that will grant their wielder unlimited power.", 
        rating=2.7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    