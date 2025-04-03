
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Insidious", 
    year=2010
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Insidious", 
        year=2010, 
        plot="A family looks to prevent evil spirits from trapping their comatose child in a realm called The Further.", 
        rating=6.8
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    