
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Maze Runner: The Scorch Trials", 
    year=2015
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Maze Runner: The Scorch Trials", 
        year=2015, 
        plot="After having escaped the Maze, the Gladers now face a new set of challenges on the open roads of a desolate landscape filled with unimaginable obstacles.", 
        rating=6.3
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    