
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Don't Fuck in the Woods", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Don't Fuck in the Woods", 
        year=2016, 
        plot="A group of friends are going on a camping trip to celebrate graduating college. But once they enter the woods, the proverbial shit starts to hit the fan.", 
        rating=2.7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    