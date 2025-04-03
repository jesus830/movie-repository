
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Orphan", 
    year=2009
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Orphan", 
        year=2009, 
        plot="A husband and wife who recently lost their baby adopt a nine year-old girl who is not nearly as innocent as she claims to be.", 
        rating=7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    