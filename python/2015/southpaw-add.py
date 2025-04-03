
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Southpaw to the database
movies.insert(
    title="Southpaw", 
    year=2015, 
    plot="Boxer Billy Hope turns to trainer Tick Wills to help him get his life back on track after losing his wife in a tragic accident and his daughter to child protection services.", 
    rating=7.4
)

# Confirm that the movie was added
movie = movies.select(
    title="Southpaw", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    