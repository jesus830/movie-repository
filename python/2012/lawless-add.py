
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Lawless to the database
movies.insert(
    title="Lawless", 
    year=2012, 
    plot="Set in Depression-era Franklin County, Virginia, a trio of bootlegging brothers are threatened by a new special deputy and other authorities angling for a cut of their profits.", 
    rating=7.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Lawless", 
    year=2012
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    