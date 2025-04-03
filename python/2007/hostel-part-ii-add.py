
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Hostel: Part II to the database
movies.insert(
    title="Hostel: Part II", 
    year=2007, 
    plot="Three American college students studying abroad are lured to a Slovakian hostel, and discover the grim reality behind it.", 
    rating=5.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Hostel: Part II", 
    year=2007
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    