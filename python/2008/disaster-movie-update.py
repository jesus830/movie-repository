
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Disaster Movie", 
    year=2008
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Disaster Movie", 
        year=2008, 
        plot="Over the course of one evening, an unsuspecting group of twenty-somethings find themselves bombarded by a series of natural disasters and catastrophic events.", 
        rating=1.9
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    