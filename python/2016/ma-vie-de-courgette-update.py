
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Ma vie de Courgette", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Ma vie de Courgette", 
        year=2016, 
        plot="After losing his mother, a young boy is sent to a foster home with other orphans his age where he begins to learn the meaning of trust and true love.", 
        rating=7.8
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    