
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Melancholia", 
    year=2011
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Melancholia", 
        year=2011, 
        plot="Two sisters find their already strained relationship challenged as a mysterious new planet threatens to collide with Earth.", 
        rating=7.1
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    