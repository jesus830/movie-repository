
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Neighbor", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Neighbor", 
        year=2016, 
        plot="Set in Cutter Mississippi, the film follows a man who discovers the dark truth about his neighbor and the secrets he may be keeping in the cellar.", 
        rating=5.8
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    