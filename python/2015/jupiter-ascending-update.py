
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Jupiter Ascending", 
    year=2015
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Jupiter Ascending", 
        year=2015, 
        plot="A young woman discovers her destiny as an heiress of intergalactic nobility and must fight to protect the inhabitants of Earth from an ancient and destructive industry.", 
        rating=5.3
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    