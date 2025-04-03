
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="I Am the Pretty Thing That Lives in the House", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="I Am the Pretty Thing That Lives in the House", 
        year=2016, 
        plot="A young nurse takes care of elderly author who lives in a haunted house.", 
        rating=4.7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    