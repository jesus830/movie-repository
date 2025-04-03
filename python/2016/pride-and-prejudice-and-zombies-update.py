
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Pride and Prejudice and Zombies", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Pride and Prejudice and Zombies", 
        year=2016, 
        plot="Five sisters in 19th century England must cope with the pressures to marry while protecting themselves from a growing population of zombies.", 
        rating=5.8
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    