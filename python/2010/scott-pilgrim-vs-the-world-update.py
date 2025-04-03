
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Scott Pilgrim vs. the World", 
    year=2010
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Scott Pilgrim vs. the World", 
        year=2010, 
        plot="Scott Pilgrim must defeat his new girlfriend's seven evil exes in order to win her heart.", 
        rating=7.5
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    