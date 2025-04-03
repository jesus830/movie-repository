
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add G.I. Joe: Retaliation to the database
movies.insert(
    title="G.I. Joe: Retaliation", 
    year=2013, 
    plot="The G.I. Joes are not only fighting their mortal enemy Cobra; they are forced to contend with threats from within the government that jeopardize their very existence.", 
    rating=5.8
)

# Confirm that the movie was added
movie = movies.select(
    title="G.I. Joe: Retaliation", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    