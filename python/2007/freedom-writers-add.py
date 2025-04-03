
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Freedom Writers to the database
movies.insert(
    title="Freedom Writers", 
    year=2007, 
    plot="A young teacher inspires her class of at-risk students to learn tolerance, apply themselves, and pursue education beyond high school.", 
    rating=7.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Freedom Writers", 
    year=2007
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    