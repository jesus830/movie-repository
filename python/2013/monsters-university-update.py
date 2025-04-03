
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Monsters University", 
    year=2013
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Monsters University", 
        year=2013, 
        plot="A look at the relationship between Mike and Sulley during their days at Monsters University -- when they weren't necessarily the best of friends.", 
        rating=7.3
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    