
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="There Will Be Blood", 
    year=2007
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="There Will Be Blood", 
        year=2007, 
        plot="A story of family, religion, hatred, oil and madness, focusing on a turn-of-the-century prospector in the early days of the business.", 
        rating=8.1
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    