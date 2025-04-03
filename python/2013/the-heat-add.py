
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Heat to the database
movies.insert(
    title="The Heat", 
    year=2013, 
    plot="An uptight FBI Special Agent is paired with a foul-mouthed Boston cop to take down a ruthless drug lord.", 
    rating=6.6
)

# Confirm that the movie was added
movie = movies.select(
    title="The Heat", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    