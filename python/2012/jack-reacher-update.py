
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Jack Reacher", 
    year=2012
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Jack Reacher", 
        year=2012, 
        plot="A homicide investigator digs deeper into a case involving a trained military sniper who shot five random victims.", 
        rating=7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    