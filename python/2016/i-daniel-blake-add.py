
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add I, Daniel Blake to the database
movies.insert(
    title="I, Daniel Blake", 
    year=2016, 
    plot="After having suffered a heart-attack, a 59-year-old carpenter must fight the bureaucratic forces of the system in order to receive Employment and Support Allowance.", 
    rating=7.9
)

# Confirm that the movie was added
movie = movies.select(
    title="I, Daniel Blake", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    