
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Other Guys to the database
movies.insert(
    title="The Other Guys", 
    year=2010, 
    plot="Two mismatched New York City detectives seize an opportunity to step up like the city's top cops whom they idolize -- only things don't quite go as planned.", 
    rating=6.7
)

# Confirm that the movie was added
movie = movies.select(
    title="The Other Guys", 
    year=2010
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    