
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Nymphomaniac: Vol. II", 
    year=2013
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Nymphomaniac: Vol. II", 
        year=2013, 
        plot="The continuation of Joe's sexually dictated life delves into the darker aspects of her adulthood, obsessions and what led to her being in Seligman's care.", 
        rating=6.7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    