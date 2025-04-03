
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Heartbreak Kid", 
    year=2007
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Heartbreak Kid", 
        year=2007, 
        plot="A newly wed man who believes he's just gotten hitched to the perfect woman encounters another lady on his honeymoon.", 
        rating=5.8
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    