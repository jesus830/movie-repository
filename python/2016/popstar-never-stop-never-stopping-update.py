
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Popstar: Never Stop Never Stopping", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Popstar: Never Stop Never Stopping", 
        year=2016, 
        plot="When it becomes clear that his solo album is a failure, a former boy band member does everything in his power to maintain his celebrity status.", 
        rating=6.7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    