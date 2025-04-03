
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add It's Only the End of the World to the database
movies.insert(
    title="It's Only the End of the World", 
    year=2016, 
    plot="Louis (Gaspard Ulliel), a terminally ill writer, returns home after a long absence to tell his family that he is dying.", 
    rating=7
)

# Confirm that the movie was added
movie = movies.select(
    title="It's Only the End of the World", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    