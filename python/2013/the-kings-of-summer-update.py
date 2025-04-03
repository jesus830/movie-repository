
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Kings of Summer", 
    year=2013
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Kings of Summer", 
        year=2013, 
        plot="Three teenage friends, in the ultimate act of independence, decide to spend their summer building a house in the woods and living off the land.", 
        rating=7.2
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    