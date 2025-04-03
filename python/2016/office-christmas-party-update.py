
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Office Christmas Party", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Office Christmas Party", 
        year=2016, 
        plot="When his uptight CEO sister threatens to shut down his branch, the branch manager throws an epic Christmas party in order to land a big client and save the day, but the party gets way out of hand...", 
        rating=5.8
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    