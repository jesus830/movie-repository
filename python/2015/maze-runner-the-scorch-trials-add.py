
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Maze Runner: The Scorch Trials to the database
movies.insert(
    title="Maze Runner: The Scorch Trials", 
    year=2015, 
    plot="After having escaped the Maze, the Gladers now face a new set of challenges on the open roads of a desolate landscape filled with unimaginable obstacles.", 
    rating=6.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Maze Runner: The Scorch Trials", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    