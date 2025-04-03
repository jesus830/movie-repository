
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Rise of the Planet of the Apes", 
    year=2011
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Rise of the Planet of the Apes", 
        year=2011, 
        plot="A substance, designed to help the brain repair itself, gives rise to a super-intelligent chimp who leads an ape uprising.", 
        rating=7.6
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    