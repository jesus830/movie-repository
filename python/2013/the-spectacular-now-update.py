
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Spectacular Now", 
    year=2013
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Spectacular Now", 
        year=2013, 
        plot="A hard-partying high school senior's philosophy on life changes when he meets the not-so-typical "nice girl."", 
        rating=7.1
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    