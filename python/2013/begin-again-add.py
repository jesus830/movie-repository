
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Begin Again to the database
movies.insert(
    title="Begin Again", 
    year=2013, 
    plot="A chance encounter between a disgraced music-business executive and a young singer-songwriter new to Manhattan turns into a promising collaboration between the two talents.", 
    rating=7.4
)

# Confirm that the movie was added
movie = movies.select(
    title="Begin Again", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    