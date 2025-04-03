
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Devil's Knot", 
    year=2013
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Devil's Knot", 
        year=2013, 
        plot="The savage murders of three young children sparks a controversial trial of three teenagers accused of killing the kids as part of a satanic ritual.", 
        rating=6.1
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    