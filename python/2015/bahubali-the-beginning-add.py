
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Bahubali: The Beginning to the database
movies.insert(
    title="Bahubali: The Beginning", 
    year=2015, 
    plot="In ancient India, an adventurous and daring man becomes involved in a decades old feud between two warring people.", 
    rating=8.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Bahubali: The Beginning", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    