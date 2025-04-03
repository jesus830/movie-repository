
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Friend Request", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Friend Request", 
        year=2016, 
        plot="When a college student unfriends a mysterious girl online, she finds herself fighting a demonic presence that wants to make her lonely by killing her closest friends.", 
        rating=5.4
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    