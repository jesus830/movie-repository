
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Hills Have Eyes", 
    year=2006
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Hills Have Eyes", 
        year=2006, 
        plot="A suburban American family is being stalked by a group of psychotic people who live in the desert, far away from civilization.", 
        rating=6.4
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    