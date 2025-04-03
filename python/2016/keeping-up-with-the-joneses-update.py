
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Keeping Up with the Joneses", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Keeping Up with the Joneses", 
        year=2016, 
        plot="A suburban couple becomes embroiled in an international espionage plot when they discover that their seemingly perfect new neighbors are government spies.", 
        rating=5.8
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    