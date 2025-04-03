
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Ghost Writer", 
    year=2010
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Ghost Writer", 
        year=2010, 
        plot="A ghostwriter hired to complete the memoirs of a former British prime minister uncovers secrets that put his own life in jeopardy.", 
        rating=7.2
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    