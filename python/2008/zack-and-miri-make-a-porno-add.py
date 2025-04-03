
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Zack and Miri Make a Porno to the database
movies.insert(
    title="Zack and Miri Make a Porno", 
    year=2008, 
    plot="Lifelong platonic friends Zack and Miri look to solve their respective cash-flow problems by making an adult film together. As the cameras roll, however, the duo begin to sense that they may have more feelings for each other than they previously thought.", 
    rating=6.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Zack and Miri Make a Porno", 
    year=2008
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    