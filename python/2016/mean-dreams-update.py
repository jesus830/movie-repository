
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Mean Dreams", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Mean Dreams", 
        year=2016, 
        plot="Follows Casey and Jonas, two teenagers desperate to escape their broken and abusive homes and examines the desperation of life on the run and the beauty of first love.", 
        rating=6.3
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    