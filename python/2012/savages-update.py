
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Savages", 
    year=2012
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Savages", 
        year=2012, 
        plot="Pot growers Ben and Chon face off against the Mexican drug cartel who kidnapped their shared girlfriend.", 
        rating=6.5
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    