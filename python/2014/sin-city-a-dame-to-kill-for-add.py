
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Sin City: A Dame to Kill For to the database
movies.insert(
    title="Sin City: A Dame to Kill For", 
    year=2014, 
    plot="Some of Sin City's most hard-boiled citizens cross paths with a few of its more reviled inhabitants.", 
    rating=6.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Sin City: A Dame to Kill For", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    