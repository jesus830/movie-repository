
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Moonlight to the database
movies.insert(
    title="Moonlight", 
    year=2016, 
    plot="A chronicle of the childhood, adolescence and burgeoning adulthood of a young, African-American, gay man growing up in a rough neighborhood of Miami.", 
    rating=7.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Moonlight", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    