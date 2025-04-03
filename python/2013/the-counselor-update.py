
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Counselor", 
    year=2013
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Counselor", 
        year=2013, 
        plot="A lawyer finds himself in over his head when he gets involved in drug trafficking.", 
        rating=5.3
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    