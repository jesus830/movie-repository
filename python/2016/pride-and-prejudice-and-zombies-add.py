
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Pride and Prejudice and Zombies to the database
movies.insert(
    title="Pride and Prejudice and Zombies", 
    year=2016, 
    plot="Five sisters in 19th century England must cope with the pressures to marry while protecting themselves from a growing population of zombies.", 
    rating=5.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Pride and Prejudice and Zombies", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    