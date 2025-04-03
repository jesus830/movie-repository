
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Theory of Everything to the database
movies.insert(
    title="The Theory of Everything", 
    year=2014, 
    plot="A look at the relationship between the famous physicist Stephen Hawking and his wife.", 
    rating=7.7
)

# Confirm that the movie was added
movie = movies.select(
    title="The Theory of Everything", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    