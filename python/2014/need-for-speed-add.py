
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Need for Speed to the database
movies.insert(
    title="Need for Speed", 
    year=2014, 
    plot="Fresh from prison, a street racer who was framed by a wealthy business associate joins a cross country race with revenge in mind. His ex-partner, learning of the plan, places a massive bounty on his head as the race begins.", 
    rating=6.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Need for Speed", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    