
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Inland Empire", 
    year=2006
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Inland Empire", 
        year=2006, 
        plot="As an actress starts to adopt the persona of her character in a film, her world starts to become nightmarish and surreal.", 
        rating=7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    