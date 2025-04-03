
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Busanhaeng to the database
movies.insert(
    title="Busanhaeng", 
    year=2016, 
    plot="While a zombie virus breaks out in South Korea, passengers struggle to survive on the train from Seoul to Busan.", 
    rating=7.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Busanhaeng", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    