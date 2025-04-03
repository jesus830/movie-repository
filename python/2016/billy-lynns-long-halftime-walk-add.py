
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Billy Lynn's Long Halftime Walk to the database
movies.insert(
    title="Billy Lynn's Long Halftime Walk", 
    year=2016, 
    plot="19-year-old Billy Lynn is brought home for a victory tour after a harrowing Iraq battle. Through flashbacks the film shows what really happened to his squad - contrasting the realities of war with America's perceptions.", 
    rating=6.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Billy Lynn's Long Halftime Walk", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    