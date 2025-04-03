
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Absolutely Anything to the database
movies.insert(
    title="Absolutely Anything", 
    year=2015, 
    plot="A group of eccentric aliens confer a human being with the power to do absolutely anything, as an experiment.", 
    rating=6
)

# Confirm that the movie was added
movie = movies.select(
    title="Absolutely Anything", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    