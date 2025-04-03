
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Spy to the database
movies.insert(
    title="Spy", 
    year=2015, 
    plot="A desk-bound CIA analyst volunteers to go undercover to infiltrate the world of a deadly arms dealer, and prevent diabolical global disaster.", 
    rating=7.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Spy", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    