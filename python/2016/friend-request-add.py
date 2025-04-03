
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Friend Request to the database
movies.insert(
    title="Friend Request", 
    year=2016, 
    plot="When a college student unfriends a mysterious girl online, she finds herself fighting a demonic presence that wants to make her lonely by killing her closest friends.", 
    rating=5.4
)

# Confirm that the movie was added
movie = movies.select(
    title="Friend Request", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    