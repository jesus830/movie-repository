
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Taken to the database
movies.insert(
    title="Taken", 
    year=2008, 
    plot="A retired CIA agent travels across Europe and relies on his old skills to save his estranged daughter, who has been kidnapped while on a trip to Paris.", 
    rating=7.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Taken", 
    year=2008
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    