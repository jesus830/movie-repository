
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Noah", 
    year=2014
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Noah", 
        year=2014, 
        plot="A man is chosen by his world's creator to undertake a momentous mission before an apocalyptic flood cleanses the world.", 
        rating=5.8
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    