
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add District 9 to the database
movies.insert(
    title="District 9", 
    year=2009, 
    plot="An extraterrestrial race forced to live in slum-like conditions on Earth suddenly finds a kindred spirit in a government agent who is exposed to their biotechnology.", 
    rating=8
)

# Confirm that the movie was added
movie = movies.select(
    title="District 9", 
    year=2009
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    