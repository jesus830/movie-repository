
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Rock of Ages", 
    year=2012
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Rock of Ages", 
        year=2012, 
        plot="A small town girl and a city boy meet on the Sunset Strip, while pursuing their Hollywood dreams.", 
        rating=5.9
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    