
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Theory of Everything", 
    year=2014
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Theory of Everything", 
        year=2014, 
        plot="A look at the relationship between the famous physicist Stephen Hawking and his wife.", 
        rating=7.7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    