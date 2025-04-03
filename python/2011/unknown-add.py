
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Unknown to the database
movies.insert(
    title="Unknown", 
    year=2011, 
    plot="A man awakens from a coma, only to discover that someone has taken on his identity and that no one, (not even his wife), believes him. With the help of a young woman, he sets out to prove who he is.", 
    rating=6.9
)

# Confirm that the movie was added
movie = movies.select(
    title="Unknown", 
    year=2011
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    