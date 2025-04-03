
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add What to Expect When You're Expecting to the database
movies.insert(
    title="What to Expect When You're Expecting", 
    year=2012, 
    plot="Follows the lives of five interconnected couples as they experience the thrills and surprises of having a baby, and realize that no matter what you plan for, life does not always deliver what is expected.", 
    rating=5.7
)

# Confirm that the movie was added
movie = movies.select(
    title="What to Expect When You're Expecting", 
    year=2012
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    