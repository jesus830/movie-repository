
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Don't Fuck in the Woods to the database
movies.insert(
    title="Don't Fuck in the Woods", 
    year=2016, 
    plot="A group of friends are going on a camping trip to celebrate graduating college. But once they enter the woods, the proverbial shit starts to hit the fan.", 
    rating=2.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Don't Fuck in the Woods", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    