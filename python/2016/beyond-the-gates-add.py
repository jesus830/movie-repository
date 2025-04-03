
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Beyond the Gates to the database
movies.insert(
    title="Beyond the Gates", 
    year=2016, 
    plot="Two estranged brothers reunite at their missing father's video store and find a VCR board game dubbed 'Beyond The Gates' that holds a connection to their father's disappearance.", 
    rating=5.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Beyond the Gates", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    