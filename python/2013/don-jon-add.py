
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Don Jon to the database
movies.insert(
    title="Don Jon", 
    year=2013, 
    plot="A New Jersey guy dedicated to his family, friends, and church, develops unrealistic expectations from watching porn and works to find happiness and intimacy with his potential true love.", 
    rating=6.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Don Jon", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    