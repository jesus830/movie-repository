
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Rocky Balboa", 
    year=2006
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Rocky Balboa", 
        year=2006, 
        plot="Thirty years after the ring of the first bell, Rocky Balboa comes out of retirement and dons his gloves for his final fight; against the reigning heavyweight champ Mason 'The Line' Dixon.", 
        rating=7.2
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    