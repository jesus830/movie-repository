
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Avatar to the database
movies.insert(
    title="Avatar", 
    year=2009, 
    plot="A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.", 
    rating=7.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Avatar", 
    year=2009
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    