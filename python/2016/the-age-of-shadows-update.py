
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Age of Shadows", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Age of Shadows", 
        year=2016, 
        plot="Japanese agents close in as members of the Korean resistance plan an attack in 1920's Seoul.", 
        rating=7.2
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    