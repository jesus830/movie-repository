
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Iris to the database
movies.insert(
    title="Iris", 
    year=2016, 
    plot="Iris, young wife of a businessman, disappears in Paris. Maybe a mechanic with many debts is involved in the strange affair. A really complicated job for the police.", 
    rating=6.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Iris", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    