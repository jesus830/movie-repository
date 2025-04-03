
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="WALL·E", 
    year=2008
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="WALL·E", 
        year=2008, 
        plot="In the distant future, a small waste-collecting robot inadvertently embarks on a space journey that will ultimately decide the fate of mankind.", 
        rating=8.4
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    