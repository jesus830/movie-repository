
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Carol to the database
movies.insert(
    title="Carol", 
    year=2015, 
    plot="An aspiring photographer develops an intimate relationship with an older woman in 1950s New York.", 
    rating=7.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Carol", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    