
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Maze Runner", 
    year=2014
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Maze Runner", 
        year=2014, 
        plot="Thomas is deposited in a community of boys after his memory is erased, soon learning they're all trapped in a maze that will require him to join forces with fellow "runners" for a shot at escape.", 
        rating=6.8
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    