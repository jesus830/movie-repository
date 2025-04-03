
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Perfume: The Story of a Murderer to the database
movies.insert(
    title="Perfume: The Story of a Murderer", 
    year=2006, 
    plot="Jean-Baptiste Grenouille, born with a superior olfactory sense, creates the world's finest perfume. His work, however, takes a dark turn as he searches for the ultimate scent.", 
    rating=7.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Perfume: The Story of a Murderer", 
    year=2006
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    