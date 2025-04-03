
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="No Strings Attached", 
    year=2011
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="No Strings Attached", 
        year=2011, 
        plot="A guy and girl try to keep their relationship strictly physical, but it's not long before they learn that they want something more.", 
        rating=6.2
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    