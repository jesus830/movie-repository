
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Great Gatsby to the database
movies.insert(
    title="The Great Gatsby", 
    year=2013, 
    plot="A writer and wall street trader, Nick, finds himself drawn to the past and lifestyle of his millionaire neighbor, Jay Gatsby.", 
    rating=7.3
)

# Confirm that the movie was added
movie = movies.select(
    title="The Great Gatsby", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    