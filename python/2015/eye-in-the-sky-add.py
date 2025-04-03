
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Eye in the Sky to the database
movies.insert(
    title="Eye in the Sky", 
    year=2015, 
    plot="Col. Katherine Powell, a military officer in command of an operation to capture terrorists in Kenya, sees her mission escalate when a girl enters the kill zone triggering an international dispute over the implications of modern warfare.", 
    rating=7.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Eye in the Sky", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    