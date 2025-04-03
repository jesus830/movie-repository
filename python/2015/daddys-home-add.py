
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Daddy's Home to the database
movies.insert(
    title="Daddy's Home", 
    year=2015, 
    plot="Brad Whitaker is a radio host trying to get his stepchildren to love him and call him Dad. But his plans turn upside down when their biological father, Dusty Mayron, returns.", 
    rating=6.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Daddy's Home", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    