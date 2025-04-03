
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Walk to the database
movies.insert(
    title="The Walk", 
    year=2015, 
    plot="In 1974, high-wire artist Philippe Petit recruits a team of people to help him realize his dream: to walk the immense void between the World Trade Center towers.", 
    rating=7.3
)

# Confirm that the movie was added
movie = movies.select(
    title="The Walk", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    