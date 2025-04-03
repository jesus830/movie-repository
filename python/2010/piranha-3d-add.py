
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Piranha 3D to the database
movies.insert(
    title="Piranha 3D", 
    year=2010, 
    plot="After a sudden underwater tremor sets free scores of the prehistoric man-eating fish, an unlikely group of strangers must band together to stop themselves from becoming fish food for the area's new razor-toothed residents.", 
    rating=5.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Piranha 3D", 
    year=2010
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    