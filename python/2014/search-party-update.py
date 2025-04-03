
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Search Party", 
    year=2014
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Search Party", 
        year=2014, 
        plot="A pair of friends embark on a mission to reunite their pal with the woman he was going to marry.", 
        rating=5.6
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    