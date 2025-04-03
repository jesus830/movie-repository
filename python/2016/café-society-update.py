
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Café Society", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Café Society", 
        year=2016, 
        plot="In the 1930s, a Bronx native moves to Hollywood and falls in love with a young woman who is seeing a married man.", 
        rating=6.7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    