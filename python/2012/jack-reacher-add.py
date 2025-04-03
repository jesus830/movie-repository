
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Jack Reacher to the database
movies.insert(
    title="Jack Reacher", 
    year=2012, 
    plot="A homicide investigator digs deeper into a case involving a trained military sniper who shot five random victims.", 
    rating=7
)

# Confirm that the movie was added
movie = movies.select(
    title="Jack Reacher", 
    year=2012
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    