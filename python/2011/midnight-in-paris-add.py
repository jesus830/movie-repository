
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Midnight in Paris to the database
movies.insert(
    title="Midnight in Paris", 
    year=2011, 
    plot="While on a trip to Paris with his fiancée's family, a nostalgic screenwriter finds himself mysteriously going back to the 1920s everyday at midnight.", 
    rating=7.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Midnight in Paris", 
    year=2011
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    