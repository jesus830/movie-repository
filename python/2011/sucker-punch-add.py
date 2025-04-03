
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Sucker Punch to the database
movies.insert(
    title="Sucker Punch", 
    year=2011, 
    plot="A young girl is institutionalized by her abusive stepfather, retreating to an alternative reality as a coping strategy, envisioning a plan to help her escape.", 
    rating=6.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Sucker Punch", 
    year=2011
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    