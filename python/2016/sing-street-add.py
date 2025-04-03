
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Sing Street to the database
movies.insert(
    title="Sing Street", 
    year=2016, 
    plot="A boy growing up in Dublin during the 1980s escapes his strained family life by starting a band to impress the mysterious girl he likes.", 
    rating=8
)

# Confirm that the movie was added
movie = movies.select(
    title="Sing Street", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    