
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Captain Phillips to the database
movies.insert(
    title="Captain Phillips", 
    year=2013, 
    plot="The true story of Captain Richard Phillips and the 2009 hijacking by Somali pirates of the U.S.-flagged MV Maersk Alabama, the first American cargo ship to be hijacked in two hundred years.", 
    rating=7.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Captain Phillips", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    