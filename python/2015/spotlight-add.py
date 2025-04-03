
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Spotlight to the database
movies.insert(
    title="Spotlight", 
    year=2015, 
    plot="The true story of how the Boston Globe uncovered the massive scandal of child molestation and cover-up within the local Catholic Archdiocese, shaking the entire Catholic Church to its core.", 
    rating=8.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Spotlight", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    