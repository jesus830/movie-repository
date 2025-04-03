
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Rogue One", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Rogue One", 
        year=2016, 
        plot="The Rebel Alliance makes a risky move to steal the plans for the Death Star, setting up the epic saga to follow.", 
        rating=7.9
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    