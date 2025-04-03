
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Frantz", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Frantz", 
        year=2016, 
        plot="In the aftermath of WWI, a young German who grieves the death of her fiancé in France meets a mysterious Frenchman who visits the fiancé's grave to lay flowers.", 
        rating=7.5
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    