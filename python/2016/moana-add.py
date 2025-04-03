
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Moana to the database
movies.insert(
    title="Moana", 
    year=2016, 
    plot="In Ancient Polynesia, when a terrible curse incurred by the Demigod Maui reaches an impetuous Chieftain's daughter's island, she answers the Ocean's call to seek out the Demigod to set things right.", 
    rating=7.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Moana", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    