
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Doctor Strange to the database
movies.insert(
    title="Doctor Strange", 
    year=2016, 
    plot="While on a journey of physical and spiritual healing, a brilliant neurosurgeon is drawn into the world of the mystic arts.", 
    rating=7.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Doctor Strange", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    