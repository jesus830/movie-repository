
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Real Steel", 
    year=2011
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Real Steel", 
        year=2011, 
        plot="In the near future, robot boxing is a top sport. A struggling promoter feels he's found a champion in a discarded robot.", 
        rating=7.1
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    