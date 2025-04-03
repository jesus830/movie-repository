
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Spectacular Now to the database
movies.insert(
    title="The Spectacular Now", 
    year=2013, 
    plot="A hard-partying high school senior's philosophy on life changes when he meets the not-so-typical "nice girl."", 
    rating=7.1
)

# Confirm that the movie was added
movie = movies.select(
    title="The Spectacular Now", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    