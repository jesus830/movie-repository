
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Child 44", 
    year=2015
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Child 44", 
        year=2015, 
        plot="A disgraced member of the Russian military police investigates a series of child murders during the Stalin-era Soviet Union.", 
        rating=6.5
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    