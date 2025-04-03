
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Mommy", 
    year=2014
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Mommy", 
        year=2014, 
        plot="A widowed single mother, raising her violent son alone, finds new hope when a mysterious neighbor inserts herself into their household.", 
        rating=8.1
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    