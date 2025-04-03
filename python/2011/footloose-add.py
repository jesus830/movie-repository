
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Footloose to the database
movies.insert(
    title="Footloose", 
    year=2011, 
    plot="City teenager Ren MacCormack moves to a small town where rock music and dancing have been banned, and his rebellious spirit shakes up the populace.", 
    rating=5.9
)

# Confirm that the movie was added
movie = movies.select(
    title="Footloose", 
    year=2011
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    