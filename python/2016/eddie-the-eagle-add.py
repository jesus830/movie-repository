
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Eddie the Eagle to the database
movies.insert(
    title="Eddie the Eagle", 
    year=2016, 
    plot="The story of Eddie Edwards, the notoriously tenacious British underdog ski jumper who charmed the world at the 1988 Winter Olympics.", 
    rating=7.4
)

# Confirm that the movie was added
movie = movies.select(
    title="Eddie the Eagle", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    