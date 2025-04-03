
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Steve Jobs", 
    year=2015
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Steve Jobs", 
        year=2015, 
        plot="Steve Jobs takes us behind the scenes of the digital revolution, to paint a portrait of the man at its epicenter. The story unfolds backstage at three iconic product launches, ending in 1998 with the unveiling of the iMac.", 
        rating=7.2
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    