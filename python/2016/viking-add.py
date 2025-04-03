
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Viking to the database
movies.insert(
    title="Viking", 
    year=2016, 
    plot="Kievan Rus, late 10th century. After the death of his father, the young Viking prince Vladimir of Novgorod is forced into exile across the frozen sea.", 
    rating=4.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Viking", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    