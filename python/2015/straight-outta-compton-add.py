
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Straight Outta Compton to the database
movies.insert(
    title="Straight Outta Compton", 
    year=2015, 
    plot="The group NWA emerges from the mean streets of Compton in Los Angeles, California, in the mid-1980s and revolutionizes Hip Hop culture with their music and tales about life in the hood.", 
    rating=7.9
)

# Confirm that the movie was added
movie = movies.select(
    title="Straight Outta Compton", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    