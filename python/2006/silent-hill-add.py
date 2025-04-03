
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Silent Hill to the database
movies.insert(
    title="Silent Hill", 
    year=2006, 
    plot="A woman, Rose, goes in search for her adopted daughter within the confines of a strange, desolate town called Silent Hill.", 
    rating=6.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Silent Hill", 
    year=2006
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    