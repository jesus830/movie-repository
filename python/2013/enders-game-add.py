
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Ender's Game to the database
movies.insert(
    title="Ender's Game", 
    year=2013, 
    plot="Young Ender Wiggin is recruited by the International Military to lead the fight against the Formics, a genocidal alien race which nearly annihilated the human race in a previous invasion.", 
    rating=6.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Ender's Game", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    