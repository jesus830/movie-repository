
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Batman v Superman: Dawn of Justice", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Batman v Superman: Dawn of Justice", 
        year=2016, 
        plot="Fearing that the actions of Superman are left unchecked, Batman takes on the Man of Steel, while the world wrestles with what kind of a hero it really needs.", 
        rating=6.7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    