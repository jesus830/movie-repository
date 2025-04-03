
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add 28 Weeks Later to the database
movies.insert(
    title="28 Weeks Later", 
    year=2007, 
    plot="Six months after the rage virus was inflicted on the population of Great Britain, the US Army helps to secure a small area of London for the survivors to repopulate and start again. But not everything goes to plan.", 
    rating=7
)

# Confirm that the movie was added
movie = movies.select(
    title="28 Weeks Later", 
    year=2007
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    