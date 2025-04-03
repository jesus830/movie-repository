
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Bahubali: The Beginning", 
    year=2015
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Bahubali: The Beginning", 
        year=2015, 
        plot="In ancient India, an adventurous and daring man becomes involved in a decades old feud between two warring people.", 
        rating=8.3
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    