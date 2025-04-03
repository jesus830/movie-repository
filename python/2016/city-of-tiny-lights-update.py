
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="City of Tiny Lights", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="City of Tiny Lights", 
        year=2016, 
        plot="In the teeming, multicultural metropolis of modern-day London, a seemingly straightforward missing-person case launches a down-at-heel private eye into a dangerous world of religious fanaticism and political intrigue.", 
        rating=5.7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    