
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="True Grit", 
    year=2010
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="True Grit", 
        year=2010, 
        plot="A tough U.S. Marshal helps a stubborn teenager track down her father's murderer.", 
        rating=7.6
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    