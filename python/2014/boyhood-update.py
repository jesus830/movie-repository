
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Boyhood", 
    year=2014
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Boyhood", 
        year=2014, 
        plot="The life of Mason, from early childhood to his arrival at college.", 
        rating=7.9
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    