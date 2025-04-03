
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Let Me In", 
    year=2010
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Let Me In", 
        year=2010, 
        plot="A bullied young boy befriends a young female vampire who lives in secrecy with her guardian.", 
        rating=7.2
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    