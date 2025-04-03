
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Family to the database
movies.insert(
    title="The Family", 
    year=2013, 
    plot="The Manzoni family, a notorious mafia clan, is relocated to Normandy, France under the witness protection program, where fitting in soon becomes challenging as their old habits die hard.", 
    rating=6.3
)

# Confirm that the movie was added
movie = movies.select(
    title="The Family", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    