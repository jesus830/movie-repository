
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Unfriended", 
    year=2014
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Unfriended", 
        year=2014, 
        plot="A group of online chat room friends find themselves haunted by a mysterious, supernatural force using the account of their dead friend.", 
        rating=5.6
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    