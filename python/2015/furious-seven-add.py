
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Furious Seven to the database
movies.insert(
    title="Furious Seven", 
    year=2015, 
    plot="Deckard Shaw seeks revenge against Dominic Toretto and his family for his comatose brother.", 
    rating=7.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Furious Seven", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    