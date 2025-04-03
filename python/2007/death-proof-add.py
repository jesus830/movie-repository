
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Death Proof to the database
movies.insert(
    title="Death Proof", 
    year=2007, 
    plot="Two separate sets of voluptuous women are stalked at different times by a scarred stuntman who uses his "death proof" cars to execute his murderous plans.", 
    rating=7.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Death Proof", 
    year=2007
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    