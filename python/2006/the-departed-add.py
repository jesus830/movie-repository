
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Departed to the database
movies.insert(
    title="The Departed", 
    year=2006, 
    plot="An undercover cop and a mole in the police attempt to identify each other while infiltrating an Irish gang in South Boston.", 
    rating=8.5
)

# Confirm that the movie was added
movie = movies.select(
    title="The Departed", 
    year=2006
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    