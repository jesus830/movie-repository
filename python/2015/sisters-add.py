
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Sisters to the database
movies.insert(
    title="Sisters", 
    year=2015, 
    plot="Two sisters decide to throw one last house party before their parents sell their family home.", 
    rating=6
)

# Confirm that the movie was added
movie = movies.select(
    title="Sisters", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    