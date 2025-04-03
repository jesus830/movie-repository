
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Pixels to the database
movies.insert(
    title="Pixels", 
    year=2015, 
    plot="When aliens misinterpret video feeds of classic arcade games as a declaration of war, they attack the Earth in the form of the video games.", 
    rating=5.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Pixels", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    