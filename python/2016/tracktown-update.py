
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Tracktown", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Tracktown", 
        year=2016, 
        plot="A young, talented, and lonely long-distance runner twists her ankle as she prepares for the Olympic Trials and must do something she's never done before: take a day off.", 
        rating=5.9
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    