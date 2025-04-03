
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Under the Skin to the database
movies.insert(
    title="Under the Skin", 
    year=2013, 
    plot="A mysterious young woman seduces lonely men in the evening hours in Scotland. However, events lead her to begin a process of self-discovery.", 
    rating=6.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Under the Skin", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    