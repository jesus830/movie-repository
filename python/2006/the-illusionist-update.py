
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Illusionist", 
    year=2006
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Illusionist", 
        year=2006, 
        plot="In turn-of-the-century Vienna, a magician uses his abilities to secure the love of a woman far above his social standing.", 
        rating=7.6
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    