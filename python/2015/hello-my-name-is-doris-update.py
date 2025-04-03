
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Hello, My Name Is Doris", 
    year=2015
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Hello, My Name Is Doris", 
        year=2015, 
        plot="A self-help seminar inspires a sixty-something woman to romantically pursue her younger co-worker.", 
        rating=6.7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    