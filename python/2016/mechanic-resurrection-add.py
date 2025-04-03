
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Mechanic: Resurrection to the database
movies.insert(
    title="Mechanic: Resurrection", 
    year=2016, 
    plot="Arthur Bishop thought he had put his murderous past behind him, until his most formidable foe kidnaps the love of his life. Now he is forced to travel the globe to complete three impossible assassinations, and do what he does best: make them look like accidents.", 
    rating=5.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Mechanic: Resurrection", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    