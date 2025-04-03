
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Nerve to the database
movies.insert(
    title="Nerve", 
    year=2016, 
    plot="A high school senior finds herself immersed in an online game of truth or dare, where her every move starts to become manipulated by an anonymous community of "watchers."", 
    rating=6.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Nerve", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    