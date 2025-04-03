
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Ratatouille", 
    year=2007
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Ratatouille", 
        year=2007, 
        plot="A rat who can cook makes an unusual alliance with a young kitchen worker at a famous restaurant.", 
        rating=8
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    