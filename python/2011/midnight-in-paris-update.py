
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Midnight in Paris", 
    year=2011
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Midnight in Paris", 
        year=2011, 
        plot="While on a trip to Paris with his fiancée's family, a nostalgic screenwriter finds himself mysteriously going back to the 1920s everyday at midnight.", 
        rating=7.7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    