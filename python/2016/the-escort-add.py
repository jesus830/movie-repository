
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Escort to the database
movies.insert(
    title="The Escort", 
    year=2016, 
    plot="Desperate for a good story, a sex-addicted journalist throws himself into the world of high-class escorts when he starts following a Stanford-educated prostitute.", 
    rating=6
)

# Confirm that the movie was added
movie = movies.select(
    title="The Escort", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    