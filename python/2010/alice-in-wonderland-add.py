
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Alice in Wonderland to the database
movies.insert(
    title="Alice in Wonderland", 
    year=2010, 
    plot="Nineteen-year-old Alice returns to the magical world from her childhood adventure, where she reunites with her old friends and learns of her true destiny: to end the Red Queen's reign of terror.", 
    rating=6.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Alice in Wonderland", 
    year=2010
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    