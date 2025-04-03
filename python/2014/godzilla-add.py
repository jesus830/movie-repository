
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Godzilla to the database
movies.insert(
    title="Godzilla", 
    year=2014, 
    plot="The world is beset by the appearance of monstrous creatures, but one of them may be the only one who can save humanity.", 
    rating=6.4
)

# Confirm that the movie was added
movie = movies.select(
    title="Godzilla", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    