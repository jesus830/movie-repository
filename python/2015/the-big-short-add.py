
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Big Short to the database
movies.insert(
    title="The Big Short", 
    year=2015, 
    plot="Four denizens in the world of high-finance predict the credit and housing bubble collapse of the mid-2000s, and decide to take on the big banks for their greed and lack of foresight.", 
    rating=7.8
)

# Confirm that the movie was added
movie = movies.select(
    title="The Big Short", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    