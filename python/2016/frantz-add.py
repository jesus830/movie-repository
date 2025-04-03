
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Frantz to the database
movies.insert(
    title="Frantz", 
    year=2016, 
    plot="In the aftermath of WWI, a young German who grieves the death of her fiancé in France meets a mysterious Frenchman who visits the fiancé's grave to lay flowers.", 
    rating=7.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Frantz", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    