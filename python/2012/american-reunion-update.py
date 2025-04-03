
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="American Reunion", 
    year=2012
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="American Reunion", 
        year=2012, 
        plot="Jim, Michelle, Stifler, and their friends reunite in East Great Falls, Michigan for their high school reunion.", 
        rating=6.7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    