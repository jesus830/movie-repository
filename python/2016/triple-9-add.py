
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Triple 9 to the database
movies.insert(
    title="Triple 9", 
    year=2016, 
    plot="A gang of criminals and corrupt cops plan the murder of a police officer in order to pull off their biggest heist yet across town.", 
    rating=6.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Triple 9", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    