
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Pacific Rim", 
    year=2013
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Pacific Rim", 
        year=2013, 
        plot="As a war between humankind and monstrous sea creatures wages on, a former pilot and a trainee are paired up to drive a seemingly obsolete special weapon in a desperate effort to save the world from the apocalypse.", 
        rating=7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    