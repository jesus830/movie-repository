
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Locke to the database
movies.insert(
    title="Locke", 
    year=2013, 
    plot="Ivan Locke, a dedicated family man and successful construction manager, receives a phone call on the eve of the biggest challenge of his career that sets in motion a series of events that threaten his carefully cultivated existence.", 
    rating=7.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Locke", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    