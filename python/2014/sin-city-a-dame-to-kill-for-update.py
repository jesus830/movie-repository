
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Sin City: A Dame to Kill For", 
    year=2014
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Sin City: A Dame to Kill For", 
        year=2014, 
        plot="Some of Sin City's most hard-boiled citizens cross paths with a few of its more reviled inhabitants.", 
        rating=6.5
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    