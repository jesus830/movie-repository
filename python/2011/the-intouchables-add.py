
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Intouchables to the database
movies.insert(
    title="The Intouchables", 
    year=2011, 
    plot="After he becomes a quadriplegic from a paragliding accident, an aristocrat hires a young man from the projects to be his caregiver.", 
    rating=8.6
)

# Confirm that the movie was added
movie = movies.select(
    title="The Intouchables", 
    year=2011
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    