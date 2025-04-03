
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Contratiempo", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Contratiempo", 
        year=2016, 
        plot="A young businessman faces a lawyer trying to prove his innocence by the assassination of his lover.", 
        rating=7.9
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    