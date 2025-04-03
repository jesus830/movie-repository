
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Dark Shadows to the database
movies.insert(
    title="Dark Shadows", 
    year=2012, 
    plot="An imprisoned vampire, Barnabas Collins, is set free and returns to his ancestral home, where his dysfunctional descendants are in need of his protection.", 
    rating=6.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Dark Shadows", 
    year=2012
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    