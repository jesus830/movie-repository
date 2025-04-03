
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Birth of the Dragon", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Birth of the Dragon", 
        year=2016, 
        plot="Young, up-and-coming martial artist, Bruce Lee, challenges legendary kung fu master Wong Jack Man to a no-holds-barred fight in Northern California.", 
        rating=3.9
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    