
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add 50/50 to the database
movies.insert(
    title="50/50", 
    year=2011, 
    plot="Inspired by a true story, a comedy centered on a 27-year-old guy who learns of his cancer diagnosis, and his subsequent struggle to beat the disease.", 
    rating=7.7
)

# Confirm that the movie was added
movie = movies.select(
    title="50/50", 
    year=2011
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    