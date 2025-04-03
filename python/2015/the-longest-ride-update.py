
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Longest Ride", 
    year=2015
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Longest Ride", 
        year=2015, 
        plot="The lives of a young couple intertwine with a much older man, as he reflects back on a past love.", 
        rating=7.1
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    