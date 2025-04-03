
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Birdman or (The Unexpected Virtue of Ignorance) to the database
movies.insert(
    title="Birdman or (The Unexpected Virtue of Ignorance)", 
    year=2014, 
    plot="Illustrated upon the progress of his latest Broadway play, a former popular actor's struggle to cope with his current life as a wasted actor is shown.", 
    rating=7.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Birdman or (The Unexpected Virtue of Ignorance)", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    