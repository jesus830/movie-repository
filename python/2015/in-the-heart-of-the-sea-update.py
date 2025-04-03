
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="In the Heart of the Sea", 
    year=2015
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="In the Heart of the Sea", 
        year=2015, 
        plot="A recounting of a New England whaling ship's sinking by a giant whale in 1820, an experience that later inspired the great novel Moby-Dick.", 
        rating=6.9
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    