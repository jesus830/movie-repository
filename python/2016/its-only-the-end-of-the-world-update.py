
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="It's Only the End of the World", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="It's Only the End of the World", 
        year=2016, 
        plot="Louis (Gaspard Ulliel), a terminally ill writer, returns home after a long absence to tell his family that he is dying.", 
        rating=7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    