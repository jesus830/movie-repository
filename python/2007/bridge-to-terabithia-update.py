
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Bridge to Terabithia", 
    year=2007
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Bridge to Terabithia", 
        year=2007, 
        plot="A preteen's life turns upside down when he befriends the new girl in school and they imagine a whole new fantasy world to escape reality.", 
        rating=7.2
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    