
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Fifty Shades of Grey to the database
movies.insert(
    title="Fifty Shades of Grey", 
    year=2015, 
    plot="Literature student Anastasia Steele's life changes forever when she meets handsome, yet tormented, billionaire Christian Grey.", 
    rating=4.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Fifty Shades of Grey", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    