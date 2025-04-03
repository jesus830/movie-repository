
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The A-Team to the database
movies.insert(
    title="The A-Team", 
    year=2010, 
    plot="A group of Iraq War veterans looks to clear their name with the U.S. military, who suspect the four men of committing a crime for which they were framed.", 
    rating=6.8
)

# Confirm that the movie was added
movie = movies.select(
    title="The A-Team", 
    year=2010
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    