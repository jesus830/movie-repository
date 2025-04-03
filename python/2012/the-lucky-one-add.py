
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Lucky One to the database
movies.insert(
    title="The Lucky One", 
    year=2012, 
    plot="A Marine travels to Louisiana after serving three tours in Iraq and searches for the unknown woman he believes was his good luck charm during the war.", 
    rating=6.5
)

# Confirm that the movie was added
movie = movies.select(
    title="The Lucky One", 
    year=2012
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    