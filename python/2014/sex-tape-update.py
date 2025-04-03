
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Sex Tape", 
    year=2014
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Sex Tape", 
        year=2014, 
        plot="A married couple wake up to discover that the sex tape they made the evening before has gone missing, leading to a frantic search for its whereabouts.", 
        rating=5.1
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    