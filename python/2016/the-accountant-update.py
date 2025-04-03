
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Accountant", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Accountant", 
        year=2016, 
        plot="As a math savant uncooks the books for a new client, the Treasury Department closes in on his activities and the body count starts to rise.", 
        rating=7.4
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    