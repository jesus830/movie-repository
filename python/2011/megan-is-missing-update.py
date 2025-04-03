
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Megan Is Missing", 
    year=2011
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Megan Is Missing", 
        year=2011, 
        plot="Two teenage girls encounter an Internet child predator.", 
        rating=4.9
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    