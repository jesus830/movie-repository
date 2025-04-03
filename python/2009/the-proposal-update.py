
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Proposal", 
    year=2009
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Proposal", 
        year=2009, 
        plot="A pushy boss forces her young assistant to marry her in order to keep her visa status in the U.S. and avoid deportation to Canada.", 
        rating=6.7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    