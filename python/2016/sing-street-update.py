
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Sing Street", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Sing Street", 
        year=2016, 
        plot="A boy growing up in Dublin during the 1980s escapes his strained family life by starting a band to impress the mysterious girl he likes.", 
        rating=8
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    