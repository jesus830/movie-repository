
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Her", 
    year=2013
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Her", 
        year=2013, 
        plot="A lonely writer develops an unlikely relationship with an operating system designed to meet his every need.", 
        rating=8
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    