
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Carrie", 
    year=2013
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Carrie", 
        year=2013, 
        plot="A shy girl, outcasted by her peers and sheltered by her religious mother, unleashes telekinetic terror on her small town after being pushed too far at her senior prom.", 
        rating=5.9
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    