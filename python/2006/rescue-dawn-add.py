
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Rescue Dawn to the database
movies.insert(
    title="Rescue Dawn", 
    year=2006, 
    plot="A U.S. fighter pilot's epic struggle of survival after being shot down on a mission over Laos during the Vietnam War.", 
    rating=7.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Rescue Dawn", 
    year=2006
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    