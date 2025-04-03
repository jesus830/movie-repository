
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Mission: Impossible - Rogue Nation", 
    year=2015
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Mission: Impossible - Rogue Nation", 
        year=2015, 
        plot="Ethan and team take on their most impossible mission yet, eradicating the Syndicate - an International rogue organization as highly skilled as they are, committed to destroying the IMF.", 
        rating=7.4
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    