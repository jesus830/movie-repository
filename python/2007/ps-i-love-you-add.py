
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add P.S. I Love You to the database
movies.insert(
    title="P.S. I Love You", 
    year=2007, 
    plot="A young widow discovers that her late husband has left her 10 messages intended to help ease her pain and start a new life.", 
    rating=7.1
)

# Confirm that the movie was added
movie = movies.select(
    title="P.S. I Love You", 
    year=2007
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    