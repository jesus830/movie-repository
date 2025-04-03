
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Toni Erdmann", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Toni Erdmann", 
        year=2016, 
        plot="A practical joking father tries to reconnect with his hard working daughter by creating an outrageous alter ego and posing as her CEO's life coach.", 
        rating=7.6
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    