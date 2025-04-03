
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Hostel: Part II", 
    year=2007
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Hostel: Part II", 
        year=2007, 
        plot="Three American college students studying abroad are lured to a Slovakian hostel, and discover the grim reality behind it.", 
        rating=5.5
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    