
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Satanic to the database
movies.insert(
    title="Satanic", 
    year=2016, 
    plot="Four friends on their way to Coachella stop off in Los Angeles to tour true-crime occult sites, only to encounter a mysterious young runaway who puts them on a terrifying path to ultimate horror.", 
    rating=3.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Satanic", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    