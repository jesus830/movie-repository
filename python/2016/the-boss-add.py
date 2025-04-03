
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Boss to the database
movies.insert(
    title="The Boss", 
    year=2016, 
    plot="A titan of industry is sent to prison after she's caught insider trading. When she emerges ready to rebrand herself as America's latest sweetheart, not everyone she screwed over is so quick to forgive and forget.", 
    rating=5.4
)

# Confirm that the movie was added
movie = movies.select(
    title="The Boss", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    