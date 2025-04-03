
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add A Cure for Wellness to the database
movies.insert(
    title="A Cure for Wellness", 
    year=2016, 
    plot="An ambitious young executive is sent to retrieve his company's CEO from an idyllic but mysterious "wellness center" at a remote location in the Swiss Alps, but soon suspects that the spa's treatments are not what they seem.", 
    rating=6.5
)

# Confirm that the movie was added
movie = movies.select(
    title="A Cure for Wellness", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    