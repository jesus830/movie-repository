
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Rocky Balboa to the database
movies.insert(
    title="Rocky Balboa", 
    year=2006, 
    plot="Thirty years after the ring of the first bell, Rocky Balboa comes out of retirement and dons his gloves for his final fight; against the reigning heavyweight champ Mason 'The Line' Dixon.", 
    rating=7.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Rocky Balboa", 
    year=2006
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    