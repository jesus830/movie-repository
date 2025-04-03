
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Nerve", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Nerve", 
        year=2016, 
        plot="A high school senior finds herself immersed in an online game of truth or dare, where her every move starts to become manipulated by an anonymous community of "watchers."", 
        rating=6.6
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    