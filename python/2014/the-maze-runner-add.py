
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Maze Runner to the database
movies.insert(
    title="The Maze Runner", 
    year=2014, 
    plot="Thomas is deposited in a community of boys after his memory is erased, soon learning they're all trapped in a maze that will require him to join forces with fellow "runners" for a shot at escape.", 
    rating=6.8
)

# Confirm that the movie was added
movie = movies.select(
    title="The Maze Runner", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    