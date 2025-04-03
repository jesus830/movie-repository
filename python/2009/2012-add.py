
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add 2012 to the database
movies.insert(
    title="2012", 
    year=2009, 
    plot="A frustrated writer struggles to keep his family alive when a series of global catastrophes threatens to annihilate mankind.", 
    rating=5.8
)

# Confirm that the movie was added
movie = movies.select(
    title="2012", 
    year=2009
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    