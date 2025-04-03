
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Captain America: Civil War", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Captain America: Civil War", 
        year=2016, 
        plot="Political interference in the Avengers' activities causes a rift between former allies Captain America and Iron Man.", 
        rating=7.9
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    