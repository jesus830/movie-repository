
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Exposed to the database
movies.insert(
    title="Exposed", 
    year=2016, 
    plot="A police detective investigates the truth behind his partner's death. The mysterious case reveals disturbing police corruption and a dangerous secret involving an unlikely young woman.", 
    rating=4.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Exposed", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    