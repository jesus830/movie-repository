
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Lone Ranger", 
    year=2013
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Lone Ranger", 
        year=2013, 
        plot="Native American warrior Tonto recounts the untold tales that transformed John Reid, a man of the law, into a legend of justice.", 
        rating=6.5
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    