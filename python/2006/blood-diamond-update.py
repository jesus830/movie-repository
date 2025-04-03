
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Blood Diamond", 
    year=2006
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Blood Diamond", 
        year=2006, 
        plot="A fisherman, a smuggler, and a syndicate of businessmen match wits over the possession of a priceless diamond.", 
        rating=8
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    