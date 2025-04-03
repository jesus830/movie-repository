
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Do-Over", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Do-Over", 
        year=2016, 
        plot="Two down-on-their-luck guys decide to fake their own deaths and start over with new identities, only to find the people they're pretending to be are in even deeper trouble.", 
        rating=5.7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    