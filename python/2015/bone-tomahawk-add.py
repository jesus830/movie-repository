
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Bone Tomahawk to the database
movies.insert(
    title="Bone Tomahawk", 
    year=2015, 
    plot="Four men set out in the Wild West to rescue a group of captives from cannibalistic cave dwellers.", 
    rating=7.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Bone Tomahawk", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    