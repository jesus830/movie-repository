
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="10 Years", 
    year=2011
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="10 Years", 
        year=2011, 
        plot="The night before their high school reunion, a group of friends realize they still haven't quite grown up in some ways.", 
        rating=6.1
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    