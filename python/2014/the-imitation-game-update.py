
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Imitation Game", 
    year=2014
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Imitation Game", 
        year=2014, 
        plot="During World War II, mathematician Alan Turing tries to crack the enigma code with help from fellow mathematicians.", 
        rating=8.1
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    