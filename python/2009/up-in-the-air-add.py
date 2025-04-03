
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Up in the Air to the database
movies.insert(
    title="Up in the Air", 
    year=2009, 
    plot="Ryan Bingham enjoys living out of a suitcase for his job traveling around the country firing people, but finds that lifestyle threatened by the presence of a potential love interest and a new hire.", 
    rating=7.4
)

# Confirm that the movie was added
movie = movies.select(
    title="Up in the Air", 
    year=2009
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    