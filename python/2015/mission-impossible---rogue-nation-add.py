
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Mission: Impossible - Rogue Nation to the database
movies.insert(
    title="Mission: Impossible - Rogue Nation", 
    year=2015, 
    plot="Ethan and team take on their most impossible mission yet, eradicating the Syndicate - an International rogue organization as highly skilled as they are, committed to destroying the IMF.", 
    rating=7.4
)

# Confirm that the movie was added
movie = movies.select(
    title="Mission: Impossible - Rogue Nation", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    