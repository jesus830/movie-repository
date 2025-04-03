
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Girl on the Train", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Girl on the Train", 
        year=2016, 
        plot="A divorcee becomes entangled in a missing persons investigation that promises to send shockwaves throughout her life.", 
        rating=6.5
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    