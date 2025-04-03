
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Old Boy to the database
movies.insert(
    title="Old Boy", 
    year=2013, 
    plot="Obsessed with vengeance, a man sets out to find out why he was kidnapped and locked into solitary confinement for twenty years without reason.", 
    rating=5.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Old Boy", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    