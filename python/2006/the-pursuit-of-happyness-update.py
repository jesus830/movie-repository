
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Pursuit of Happyness", 
    year=2006
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Pursuit of Happyness", 
        year=2006, 
        plot="A struggling salesman takes custody of his son as he's poised to begin a life-changing professional career.", 
        rating=8
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    