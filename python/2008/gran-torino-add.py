
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Gran Torino to the database
movies.insert(
    title="Gran Torino", 
    year=2008, 
    plot="Disgruntled Korean War veteran Walt Kowalski sets out to reform his neighbor, a Hmong teenager who tried to steal Kowalski's prized possession: a 1972 Gran Torino.", 
    rating=8.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Gran Torino", 
    year=2008
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    