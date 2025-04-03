
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Tracktown to the database
movies.insert(
    title="Tracktown", 
    year=2016, 
    plot="A young, talented, and lonely long-distance runner twists her ankle as she prepares for the Olympic Trials and must do something she's never done before: take a day off.", 
    rating=5.9
)

# Confirm that the movie was added
movie = movies.select(
    title="Tracktown", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    