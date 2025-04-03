
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Revenant to the database
movies.insert(
    title="The Revenant", 
    year=2015, 
    plot="A frontiersman on a fur trading expedition in the 1820s fights for survival after being mauled by a bear and left for dead by members of his own hunting team.", 
    rating=8
)

# Confirm that the movie was added
movie = movies.select(
    title="The Revenant", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    