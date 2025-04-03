
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="G.I. Joe: Retaliation", 
    year=2013
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="G.I. Joe: Retaliation", 
        year=2013, 
        plot="The G.I. Joes are not only fighting their mortal enemy Cobra; they are forced to contend with threats from within the government that jeopardize their very existence.", 
        rating=5.8
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    