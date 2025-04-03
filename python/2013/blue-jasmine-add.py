
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Blue Jasmine to the database
movies.insert(
    title="Blue Jasmine", 
    year=2013, 
    plot="A New York socialite, deeply troubled and in denial, arrives in San Francisco to impose upon her sister. She looks a million, but isn't bringing money, peace, or love...", 
    rating=7.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Blue Jasmine", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    