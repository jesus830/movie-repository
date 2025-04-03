
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Good Kids to the database
movies.insert(
    title="Good Kids", 
    year=2016, 
    plot="Four high school students look to redefine themselves after graduation.", 
    rating=6.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Good Kids", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    