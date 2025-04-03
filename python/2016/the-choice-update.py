
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Choice", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Choice", 
        year=2016, 
        plot="Travis and Gabby first meet as neighbors in a small coastal town and wind up in a relationship that is tested by life's most defining events.", 
        rating=6.6
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    