
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Little Miss Sunshine", 
    year=2006
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Little Miss Sunshine", 
        year=2006, 
        plot="A family determined to get their young daughter into the finals of a beauty pageant take a cross-country trip in their VW bus.", 
        rating=7.8
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    