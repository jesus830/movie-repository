
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add (500) Days of Summer to the database
movies.insert(
    title="(500) Days of Summer", 
    year=2009, 
    plot="An offbeat romantic comedy about a woman who doesn't believe true love exists, and the young man who falls for her.", 
    rating=7.7
)

# Confirm that the movie was added
movie = movies.select(
    title="(500) Days of Summer", 
    year=2009
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    