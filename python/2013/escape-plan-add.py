
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Escape Plan to the database
movies.insert(
    title="Escape Plan", 
    year=2013, 
    plot="When a structural-security authority finds himself set up and incarcerated in the world's most secret and secure prison, he has to use his skills to escape with help from the inside.", 
    rating=6.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Escape Plan", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    