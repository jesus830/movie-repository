
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Amazing Spider-Man 2 to the database
movies.insert(
    title="The Amazing Spider-Man 2", 
    year=2014, 
    plot="When New York is put under siege by Oscorp, it is up to Spider-Man to save the city he swore to protect as well as his loved ones.", 
    rating=6.7
)

# Confirm that the movie was added
movie = movies.select(
    title="The Amazing Spider-Man 2", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    