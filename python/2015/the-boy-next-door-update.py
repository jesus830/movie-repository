
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Boy Next Door", 
    year=2015
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Boy Next Door", 
        year=2015, 
        plot="A woman, separated from her unfaithful husband, falls for a younger man who has moved in next door, but their torrid affair soon takes a dangerous turn.", 
        rating=4.6
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    