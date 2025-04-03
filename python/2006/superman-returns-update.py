
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Superman Returns", 
    year=2006
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Superman Returns", 
        year=2006, 
        plot="Superman reappears after a long absence, but is challenged by an old foe who uses Kryptonian technology for world domination.", 
        rating=6.1
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    