
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="3 Days to Kill", 
    year=2014
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="3 Days to Kill", 
        year=2014, 
        plot="A dying CIA agent trying to reconnect with his estranged daughter is offered an experimental drug that could save his life in exchange for one last assignment.", 
        rating=6.2
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    