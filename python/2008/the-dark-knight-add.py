
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Dark Knight to the database
movies.insert(
    title="The Dark Knight", 
    year=2008, 
    plot="When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, the Dark Knight must come to terms with one of the greatest psychological tests of his ability to fight injustice.", 
    rating=9
)

# Confirm that the movie was added
movie = movies.select(
    title="The Dark Knight", 
    year=2008
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    