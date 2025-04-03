
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Django Unchained", 
    year=2012
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Django Unchained", 
        year=2012, 
        plot="With the help of a German bounty hunter , a freed slave sets out to rescue his wife from a brutal Mississippi plantation owner.", 
        rating=8.4
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    