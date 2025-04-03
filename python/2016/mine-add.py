
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Mine to the database
movies.insert(
    title="Mine", 
    year=2016, 
    plot="After a failed assassination attempt, a soldier finds himself stranded in the desert. Exposed to the elements, he must survive the dangers of the desert and battle the psychological and physical tolls of the treacherous conditions.", 
    rating=6
)

# Confirm that the movie was added
movie = movies.select(
    title="Mine", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    