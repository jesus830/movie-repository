
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Deuces to the database
movies.insert(
    title="Deuces", 
    year=2016, 
    plot="An agent infiltrates a crime ring ran by a charismatic boss.", 
    rating=6.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Deuces", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    