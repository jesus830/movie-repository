
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="P.S. I Love You", 
    year=2007
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="P.S. I Love You", 
        year=2007, 
        plot="A young widow discovers that her late husband has left her 10 messages intended to help ease her pain and start a new life.", 
        rating=7.1
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    