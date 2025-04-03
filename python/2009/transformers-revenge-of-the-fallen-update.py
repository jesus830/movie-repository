
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Transformers: Revenge of the Fallen", 
    year=2009
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Transformers: Revenge of the Fallen", 
        year=2009, 
        plot="Sam Witwicky leaves the Autobots behind for a normal life. But when his mind is filled with cryptic symbols, the Decepticons target him and he is dragged back into the Transformers' war.", 
        rating=6
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    