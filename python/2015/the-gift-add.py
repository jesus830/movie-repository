
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Gift to the database
movies.insert(
    title="The Gift", 
    year=2015, 
    plot="A young married couple's lives are thrown into a harrowing tailspin when an acquaintance from the husband's past brings mysterious gifts and a horrifying secret to light after more than 20 years.", 
    rating=7.1
)

# Confirm that the movie was added
movie = movies.select(
    title="The Gift", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    