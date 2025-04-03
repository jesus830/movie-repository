
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Nymphomaniac: Vol. II to the database
movies.insert(
    title="Nymphomaniac: Vol. II", 
    year=2013, 
    plot="The continuation of Joe's sexually dictated life delves into the darker aspects of her adulthood, obsessions and what led to her being in Seligman's care.", 
    rating=6.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Nymphomaniac: Vol. II", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    