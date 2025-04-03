
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Ridiculous 6", 
    year=2015
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Ridiculous 6", 
        year=2015, 
        plot="An outlaw who was raised by Native Americans discovers that he has five half-brothers; together the men go on a mission to find their wayward, deadbeat dad.", 
        rating=4.8
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    