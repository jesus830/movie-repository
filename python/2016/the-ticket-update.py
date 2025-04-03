
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Ticket", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Ticket", 
        year=2016, 
        plot="A blind man who regains his vision finds himself becoming metaphorically blinded by his obsession for the superficial.", 
        rating=5.4
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    