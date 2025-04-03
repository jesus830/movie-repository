
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Blackcoat's Daughter", 
    year=2015
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Blackcoat's Daughter", 
        year=2015, 
        plot="Two girls must battle a mysterious evil force when they get left behind at their boarding school over winter break.", 
        rating=5.6
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    