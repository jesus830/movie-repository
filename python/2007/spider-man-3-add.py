
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Spider-Man 3 to the database
movies.insert(
    title="Spider-Man 3", 
    year=2007, 
    plot="A strange black entity from another world bonds with Peter Parker and causes inner turmoil as he contends with new villains, temptations, and revenge.", 
    rating=6.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Spider-Man 3", 
    year=2007
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    