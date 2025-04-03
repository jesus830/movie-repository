
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Demain tout commence", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Demain tout commence", 
        year=2016, 
        plot="Samuel parties hard in the Marseille area of France and is awoken one morning by a woman carrying a baby she claims is his. She drives off leaving him with a wailing infant; he gives chase ... See full summary »", 
        rating=7.4
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    