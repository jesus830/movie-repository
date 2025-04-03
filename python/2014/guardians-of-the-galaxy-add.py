
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Guardians of the Galaxy to the database
movies.insert(
    title="Guardians of the Galaxy", 
    year=2014, 
    plot="A group of intergalactic criminals are forced to work together to stop a fanatical warrior from taking control of the universe.", 
    rating=8.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Guardians of the Galaxy", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    