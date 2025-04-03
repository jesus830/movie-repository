
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Fences", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Fences", 
        year=2016, 
        plot="A working-class African-American father tries to raise his family in the 1950s, while coming to terms with the events of his life.", 
        rating=7.3
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    