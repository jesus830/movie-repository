
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Gravity", 
    year=2013
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Gravity", 
        year=2013, 
        plot="Two astronauts work together to survive after an accident which leaves them alone in space.", 
        rating=7.8
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    