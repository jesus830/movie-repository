
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Transpecos", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Transpecos", 
        year=2016, 
        plot="For three Border Patrol agents working a remote desert checkpoint, the contents of one car will reveal an insidious plot within their own ranks. The next 24 hours will take them on a treacherous journey that could cost them their lives.", 
        rating=5.8
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    