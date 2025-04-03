
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Heat", 
    year=2013
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Heat", 
        year=2013, 
        plot="An uptight FBI Special Agent is paired with a foul-mouthed Boston cop to take down a ruthless drug lord.", 
        rating=6.6
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    