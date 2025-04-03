
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Nice Guys to the database
movies.insert(
    title="The Nice Guys", 
    year=2016, 
    plot="In 1970s Los Angeles, a mismatched pair of private eyes investigate a missing girl and the mysterious death of a porn star.", 
    rating=7.4
)

# Confirm that the movie was added
movie = movies.select(
    title="The Nice Guys", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    