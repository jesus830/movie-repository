
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Män som hatar kvinnor", 
    year=2009
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Män som hatar kvinnor", 
        year=2009, 
        plot="A journalist is aided in his search for a woman who has been missing -- or dead -- for forty years by a young female hacker.", 
        rating=7.8
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    