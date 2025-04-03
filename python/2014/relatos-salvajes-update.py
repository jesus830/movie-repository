
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Relatos salvajes", 
    year=2014
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Relatos salvajes", 
        year=2014, 
        plot="Six short stories that explore the extremities of human behavior involving people in distress.", 
        rating=8.1
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    