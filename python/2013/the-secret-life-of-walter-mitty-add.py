
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Secret Life of Walter Mitty to the database
movies.insert(
    title="The Secret Life of Walter Mitty", 
    year=2013, 
    plot="When his job along with that of his co-worker are threatened, Walter takes action in the real world embarking on a global journey that turns into an adventure more extraordinary than anything he could have ever imagined.", 
    rating=7.3
)

# Confirm that the movie was added
movie = movies.select(
    title="The Secret Life of Walter Mitty", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    