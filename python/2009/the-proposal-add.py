
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Proposal to the database
movies.insert(
    title="The Proposal", 
    year=2009, 
    plot="A pushy boss forces her young assistant to marry her in order to keep her visa status in the U.S. and avoid deportation to Canada.", 
    rating=6.7
)

# Confirm that the movie was added
movie = movies.select(
    title="The Proposal", 
    year=2009
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    