
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add All We Had to the database
movies.insert(
    title="All We Had", 
    year=2016, 
    plot="A mother struggles to make a better life for her daughter.", 
    rating=5.8
)

# Confirm that the movie was added
movie = movies.select(
    title="All We Had", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    