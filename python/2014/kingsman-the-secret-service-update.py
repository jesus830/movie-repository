
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Kingsman: The Secret Service", 
    year=2014
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Kingsman: The Secret Service", 
        year=2014, 
        plot="A spy organization recruits an unrefined, but promising street kid into the agency's ultra-competitive training program, just as a global threat emerges from a twisted tech genius.", 
        rating=7.7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    