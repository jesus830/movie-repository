
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Trainwreck", 
    year=2015
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Trainwreck", 
        year=2015, 
        plot="Having thought that monogamy was never possible, a commitment-phobic career woman may have to face her fears when she meets a good guy.", 
        rating=6.3
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    