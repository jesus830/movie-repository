
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Inside Out to the database
movies.insert(
    title="Inside Out", 
    year=2015, 
    plot="After young Riley is uprooted from her Midwest life and moved to San Francisco, her emotions - Joy, Fear, Anger, Disgust and Sadness - conflict on how best to navigate a new city, house, and school.", 
    rating=8.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Inside Out", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    