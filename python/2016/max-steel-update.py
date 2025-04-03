
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Max Steel", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Max Steel", 
        year=2016, 
        plot="The adventures of teenager Max McGrath and his alien companion, Steel, who must harness and combine their tremendous new powers to evolve into the turbo-charged superhero Max Steel.", 
        rating=4.6
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    