
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Edge of Tomorrow to the database
movies.insert(
    title="Edge of Tomorrow", 
    year=2014, 
    plot="A soldier fighting aliens gets to relive the same day over and over again, the day restarting every time he dies.", 
    rating=7.9
)

# Confirm that the movie was added
movie = movies.select(
    title="Edge of Tomorrow", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    