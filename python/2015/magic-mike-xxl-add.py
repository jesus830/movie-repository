
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Magic Mike XXL to the database
movies.insert(
    title="Magic Mike XXL", 
    year=2015, 
    plot="Three years after Mike bowed out of the stripper life at the top of his game, he and the remaining Kings of Tampa hit the road to Myrtle Beach to put on one last blow-out performance.", 
    rating=5.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Magic Mike XXL", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    