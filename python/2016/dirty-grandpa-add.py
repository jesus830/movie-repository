
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Dirty Grandpa to the database
movies.insert(
    title="Dirty Grandpa", 
    year=2016, 
    plot="Right before his wedding, an uptight guy is tricked into driving his grandfather, a lecherous former Army Lieutenant-Colonel, to Florida for spring break.", 
    rating=6
)

# Confirm that the movie was added
movie = movies.select(
    title="Dirty Grandpa", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    