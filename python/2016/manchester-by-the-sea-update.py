
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Manchester by the Sea", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Manchester by the Sea", 
        year=2016, 
        plot="A depressed uncle is asked to take care of his teenage nephew after the boy's father dies.", 
        rating=7.9
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    