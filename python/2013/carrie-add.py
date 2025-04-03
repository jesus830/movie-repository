
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Carrie to the database
movies.insert(
    title="Carrie", 
    year=2013, 
    plot="A shy girl, outcasted by her peers and sheltered by her religious mother, unleashes telekinetic terror on her small town after being pushed too far at her senior prom.", 
    rating=5.9
)

# Confirm that the movie was added
movie = movies.select(
    title="Carrie", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    