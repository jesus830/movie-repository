
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Hateful Eight to the database
movies.insert(
    title="The Hateful Eight", 
    year=2015, 
    plot="In the dead of a Wyoming winter, a bounty hunter and his prisoner find shelter in a cabin currently inhabited by a collection of nefarious characters.", 
    rating=7.8
)

# Confirm that the movie was added
movie = movies.select(
    title="The Hateful Eight", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    