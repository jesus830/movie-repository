
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Their Finest", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Their Finest", 
        year=2016, 
        plot="A former secretary, newly appointed as a scriptwriter for propaganda films, joins the cast and crew of a major production while the Blitz rages around them.", 
        rating=7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    