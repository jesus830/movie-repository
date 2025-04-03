
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Insidious to the database
movies.insert(
    title="Insidious", 
    year=2010, 
    plot="A family looks to prevent evil spirits from trapping their comatose child in a realm called The Further.", 
    rating=6.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Insidious", 
    year=2010
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    