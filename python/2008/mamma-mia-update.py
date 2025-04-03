
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Mamma Mia!", 
    year=2008
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Mamma Mia!", 
        year=2008, 
        plot="The story of a bride-to-be trying to find her real father told using hit songs by the popular '70s group ABBA.", 
        rating=6.4
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    