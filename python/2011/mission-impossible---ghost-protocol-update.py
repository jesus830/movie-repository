
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Mission: Impossible - Ghost Protocol", 
    year=2011
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Mission: Impossible - Ghost Protocol", 
        year=2011, 
        plot="The IMF is shut down when it's implicated in the bombing of the Kremlin, causing Ethan Hunt and his new team to go rogue to clear their organization's name.", 
        rating=7.4
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    