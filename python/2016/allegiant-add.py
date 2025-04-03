
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Allegiant to the database
movies.insert(
    title="Allegiant", 
    year=2016, 
    plot="After the earth-shattering revelations of Insurgent, Tris must escape with Four beyond the wall that encircles Chicago, to finally discover the shocking truth of the world around them.", 
    rating=5.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Allegiant", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    