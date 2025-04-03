
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Master to the database
movies.insert(
    title="The Master", 
    year=2012, 
    plot="A Naval veteran arrives home from war unsettled and uncertain of his future - until he is tantalized by The Cause and its charismatic leader.", 
    rating=7.1
)

# Confirm that the movie was added
movie = movies.select(
    title="The Master", 
    year=2012
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    