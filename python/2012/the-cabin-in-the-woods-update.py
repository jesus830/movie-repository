
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Cabin in the Woods", 
    year=2012
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Cabin in the Woods", 
        year=2012, 
        plot="Five friends go for a break at a remote cabin, where they get more than they bargained for, discovering the truth behind the cabin in the woods.", 
        rating=7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    