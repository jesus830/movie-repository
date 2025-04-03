
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Their Finest to the database
movies.insert(
    title="Their Finest", 
    year=2016, 
    plot="A former secretary, newly appointed as a scriptwriter for propaganda films, joins the cast and crew of a major production while the Blitz rages around them.", 
    rating=7
)

# Confirm that the movie was added
movie = movies.select(
    title="Their Finest", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    