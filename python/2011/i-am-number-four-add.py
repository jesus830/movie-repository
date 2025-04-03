
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add I Am Number Four to the database
movies.insert(
    title="I Am Number Four", 
    year=2011, 
    plot="Aliens and their Guardians are hiding on Earth from intergalactic bounty hunters. They can only be killed in numerical order, and Number Four is next on the list. This is his story.", 
    rating=6.1
)

# Confirm that the movie was added
movie = movies.select(
    title="I Am Number Four", 
    year=2011
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    