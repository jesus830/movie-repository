
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Deepwater Horizon to the database
movies.insert(
    title="Deepwater Horizon", 
    year=2016, 
    plot="A dramatization of the April 2010 disaster, when the offshore drilling rig Deepwater Horizon exploded and created the worst oil spill in U.S. history.", 
    rating=7.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Deepwater Horizon", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    