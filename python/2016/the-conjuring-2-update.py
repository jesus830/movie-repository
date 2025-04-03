
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Conjuring 2", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Conjuring 2", 
        year=2016, 
        plot="Lorraine and Ed Warren travel to north London to help a single mother raising four children alone in a house plagued by a malicious spirit.", 
        rating=7.4
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    