
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Victor Frankenstein to the database
movies.insert(
    title="Victor Frankenstein", 
    year=2015, 
    plot="Told from Igor's perspective, we see the troubled young assistant's dark origins, his redemptive friendship with the young medical student Viktor Von Frankenstein, and become eyewitnesses to the emergence of how Frankenstein became the man - and the legend - we know today.", 
    rating=6
)

# Confirm that the movie was added
movie = movies.select(
    title="Victor Frankenstein", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    