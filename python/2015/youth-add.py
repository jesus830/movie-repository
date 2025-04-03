
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Youth to the database
movies.insert(
    title="Youth", 
    year=2015, 
    plot="A retired orchestra conductor is on holiday with his daughter and his film director best friend in the Alps when he receives an invitation from Queen Elizabeth II to perform for Prince Philip's birthday.", 
    rating=7.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Youth", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    