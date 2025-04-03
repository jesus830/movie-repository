
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Sausage Party", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Sausage Party", 
        year=2016, 
        plot="A sausage strives to discover the truth about his existence.", 
        rating=6.3
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    