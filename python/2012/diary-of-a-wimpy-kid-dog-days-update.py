
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Diary of a Wimpy Kid: Dog Days", 
    year=2012
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Diary of a Wimpy Kid: Dog Days", 
        year=2012, 
        plot="School's out. Summer vacation is on. However, Greg may not have the best summer vacation ever. What could go wrong?", 
        rating=6.4
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    