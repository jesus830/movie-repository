
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Mission: Impossible - Ghost Protocol to the database
movies.insert(
    title="Mission: Impossible - Ghost Protocol", 
    year=2011, 
    plot="The IMF is shut down when it's implicated in the bombing of the Kremlin, causing Ethan Hunt and his new team to go rogue to clear their organization's name.", 
    rating=7.4
)

# Confirm that the movie was added
movie = movies.select(
    title="Mission: Impossible - Ghost Protocol", 
    year=2011
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    