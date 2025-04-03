
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Django Unchained to the database
movies.insert(
    title="Django Unchained", 
    year=2012, 
    plot="With the help of a German bounty hunter , a freed slave sets out to rescue his wife from a brutal Mississippi plantation owner.", 
    rating=8.4
)

# Confirm that the movie was added
movie = movies.select(
    title="Django Unchained", 
    year=2012
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    