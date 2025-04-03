
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add City of Tiny Lights to the database
movies.insert(
    title="City of Tiny Lights", 
    year=2016, 
    plot="In the teeming, multicultural metropolis of modern-day London, a seemingly straightforward missing-person case launches a down-at-heel private eye into a dangerous world of religious fanaticism and political intrigue.", 
    rating=5.7
)

# Confirm that the movie was added
movie = movies.select(
    title="City of Tiny Lights", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    