
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Finding Dory to the database
movies.insert(
    title="Finding Dory", 
    year=2016, 
    plot="The friendly but forgetful blue tang fish, Dory, begins a search for her long-lost parents, and everyone learns a few things about the real meaning of family along the way.", 
    rating=7.4
)

# Confirm that the movie was added
movie = movies.select(
    title="Finding Dory", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    