
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Star Trek Into Darkness to the database
movies.insert(
    title="Star Trek Into Darkness", 
    year=2013, 
    plot="After the crew of the Enterprise find an unstoppable force of terror from within their own organization, Captain Kirk leads a manhunt to a war-zone world to capture a one-man weapon of mass destruction.", 
    rating=7.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Star Trek Into Darkness", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    