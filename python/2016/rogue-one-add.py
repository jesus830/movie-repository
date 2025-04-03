
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Rogue One to the database
movies.insert(
    title="Rogue One", 
    year=2016, 
    plot="The Rebel Alliance makes a risky move to steal the plans for the Death Star, setting up the epic saga to follow.", 
    rating=7.9
)

# Confirm that the movie was added
movie = movies.select(
    title="Rogue One", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    