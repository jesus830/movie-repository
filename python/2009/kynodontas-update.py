
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Kynodontas", 
    year=2009
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Kynodontas", 
        year=2009, 
        plot="Three teenagers live isolated, without leaving their house, because their over-protective parents say they can only leave when their dogtooth falls out.", 
        rating=7.3
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    