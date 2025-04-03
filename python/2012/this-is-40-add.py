
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add This Is 40 to the database
movies.insert(
    title="This Is 40", 
    year=2012, 
    plot="Pete and Debbie are both about to turn 40, their kids hate each other, both of their businesses are failing, they're on the verge of losing their house, and their relationship is threatening to fall apart.", 
    rating=6.2
)

# Confirm that the movie was added
movie = movies.select(
    title="This Is 40", 
    year=2012
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    