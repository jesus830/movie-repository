
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Swiss Army Man", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Swiss Army Man", 
        year=2016, 
        plot="A hopeless man stranded on a deserted island befriends a dead body and together they go on a surreal journey to get home.", 
        rating=7.1
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    