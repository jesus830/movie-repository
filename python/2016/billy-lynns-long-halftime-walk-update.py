
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Billy Lynn's Long Halftime Walk", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Billy Lynn's Long Halftime Walk", 
        year=2016, 
        plot="19-year-old Billy Lynn is brought home for a victory tour after a harrowing Iraq battle. Through flashbacks the film shows what really happened to his squad - contrasting the realities of war with America's perceptions.", 
        rating=6.3
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    