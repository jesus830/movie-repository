
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Nine Lives", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Nine Lives", 
        year=2016, 
        plot="A stuffy businessman finds himself trapped inside the body of his family's cat.", 
        rating=5.3
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    