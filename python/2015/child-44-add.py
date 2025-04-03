
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Child 44 to the database
movies.insert(
    title="Child 44", 
    year=2015, 
    plot="A disgraced member of the Russian military police investigates a series of child murders during the Stalin-era Soviet Union.", 
    rating=6.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Child 44", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    