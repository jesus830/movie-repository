
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add White House Down to the database
movies.insert(
    title="White House Down", 
    year=2013, 
    plot="While on a tour of the White House with his young daughter, a Capitol policeman springs into action to save his child and protect the president from a heavily armed group of paramilitary invaders.", 
    rating=6.4
)

# Confirm that the movie was added
movie = movies.select(
    title="White House Down", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    