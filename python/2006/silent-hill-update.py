
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Silent Hill", 
    year=2006
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Silent Hill", 
        year=2006, 
        plot="A woman, Rose, goes in search for her adopted daughter within the confines of a strange, desolate town called Silent Hill.", 
        rating=6.6
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    