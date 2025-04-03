
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Triple 9", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Triple 9", 
        year=2016, 
        plot="A gang of criminals and corrupt cops plan the murder of a police officer in order to pull off their biggest heist yet across town.", 
        rating=6.3
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    