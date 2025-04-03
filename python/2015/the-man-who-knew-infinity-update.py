
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Man Who Knew Infinity", 
    year=2015
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Man Who Knew Infinity", 
        year=2015, 
        plot="The story of the life and academic career of the pioneer Indian mathematician, Srinivasa Ramanujan, and his friendship with his mentor, Professor G.H. Hardy.", 
        rating=7.2
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    