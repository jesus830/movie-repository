
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Handsome Devil to the database
movies.insert(
    title="Handsome Devil", 
    year=2016, 
    plot="Ned and Conor are forced to share a bedroom at their boarding school. The loner and the star athlete at this rugby-mad school form an unlikely friendship until it's tested by the authorities.", 
    rating=7.4
)

# Confirm that the movie was added
movie = movies.select(
    title="Handsome Devil", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    