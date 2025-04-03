
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Super 8", 
    year=2011
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Super 8", 
        year=2011, 
        plot="During the summer of 1979, a group of friends witness a train crash and investigate subsequent unexplained events in their small town.", 
        rating=7.1
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    