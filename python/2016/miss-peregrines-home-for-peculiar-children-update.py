
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Miss Peregrine's Home for Peculiar Children", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Miss Peregrine's Home for Peculiar Children", 
        year=2016, 
        plot="When Jacob discovers clues to a mystery that stretches across time, he finds Miss Peregrine's Home for Peculiar Children. But the danger deepens after he gets to know the residents and learns about their special powers.", 
        rating=6.7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    