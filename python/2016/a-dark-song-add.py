
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add A Dark Song to the database
movies.insert(
    title="A Dark Song", 
    year=2016, 
    plot="A determined young woman and a damaged occultist risk their lives and souls to perform a dangerous ritual that will grant them what they want.", 
    rating=6.1
)

# Confirm that the movie was added
movie = movies.select(
    title="A Dark Song", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    