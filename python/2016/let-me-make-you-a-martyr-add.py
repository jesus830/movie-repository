
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Let Me Make You a Martyr to the database
movies.insert(
    title="Let Me Make You a Martyr", 
    year=2016, 
    plot="A cerebral revenge film about two adopted siblings who fall in love, and hatch a plan to kill their abusive father.", 
    rating=6.4
)

# Confirm that the movie was added
movie = movies.select(
    title="Let Me Make You a Martyr", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    