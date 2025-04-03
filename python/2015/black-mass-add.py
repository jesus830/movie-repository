
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Black Mass to the database
movies.insert(
    title="Black Mass", 
    year=2015, 
    plot="The true story of Whitey Bulger, the brother of a state senator and the most infamous violent criminal in the history of South Boston, who became an FBI informant to take down a Mafia family invading his turf.", 
    rating=6.9
)

# Confirm that the movie was added
movie = movies.select(
    title="Black Mass", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    