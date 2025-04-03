
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="How to Be Single", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="How to Be Single", 
        year=2016, 
        plot="A group of young adults navigate love and relationships in New York City.", 
        rating=6.1
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    