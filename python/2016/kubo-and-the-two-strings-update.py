
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Kubo and the Two Strings", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Kubo and the Two Strings", 
        year=2016, 
        plot="A young boy named Kubo must locate a magical suit of armour worn by his late father in order to defeat a vengeful spirit from the past.", 
        rating=7.9
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    