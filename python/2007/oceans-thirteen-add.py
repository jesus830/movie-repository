
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Ocean's Thirteen to the database
movies.insert(
    title="Ocean's Thirteen", 
    year=2007, 
    plot="Danny Ocean rounds up the boys for a third heist, after casino owner Willy Bank double-crosses one of the original eleven, Reuben Tishkoff.", 
    rating=6.9
)

# Confirm that the movie was added
movie = movies.select(
    title="Ocean's Thirteen", 
    year=2007
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    