
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Prometheus to the database
movies.insert(
    title="Prometheus", 
    year=2012, 
    plot="Following clues to the origin of mankind, a team finds a structure on a distant moon, but they soon realize they are not alone.", 
    rating=7
)

# Confirm that the movie was added
movie = movies.select(
    title="Prometheus", 
    year=2012
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    