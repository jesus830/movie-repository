
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Loving to the database
movies.insert(
    title="Loving", 
    year=2016, 
    plot="The story of Richard and Mildred Loving, a couple whose arrest for interracial marriage in 1960s Virginia began a legal battle that would end with the Supreme Court's historic 1967 decision.", 
    rating=7.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Loving", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    