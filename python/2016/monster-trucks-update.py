
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Monster Trucks", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Monster Trucks", 
        year=2016, 
        plot="A young man working at a small town junkyard discovers and befriends a creature which feeds on oil being sought by a fracking company.", 
        rating=5.7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    