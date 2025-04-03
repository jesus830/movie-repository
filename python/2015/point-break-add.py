
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Point Break to the database
movies.insert(
    title="Point Break", 
    year=2015, 
    plot="A young FBI agent infiltrates an extraordinary team of extreme sports athletes he suspects of masterminding a string of unprecedented, sophisticated corporate heists.", 
    rating=5.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Point Break", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    