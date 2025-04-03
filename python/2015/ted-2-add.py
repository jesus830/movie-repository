
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Ted 2 to the database
movies.insert(
    title="Ted 2", 
    year=2015, 
    plot="Newlywed couple Ted and Tami-Lynn want to have a baby, but in order to qualify to be a parent, Ted will have to prove he's a person in a court of law.", 
    rating=6.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Ted 2", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    