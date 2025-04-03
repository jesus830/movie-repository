
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Steve Jobs to the database
movies.insert(
    title="Steve Jobs", 
    year=2015, 
    plot="Steve Jobs takes us behind the scenes of the digital revolution, to paint a portrait of the man at its epicenter. The story unfolds backstage at three iconic product launches, ending in 1998 with the unveiling of the iMac.", 
    rating=7.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Steve Jobs", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    