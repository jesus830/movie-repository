
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Shut In to the database
movies.insert(
    title="Shut In", 
    year=2016, 
    plot="A heart-pounding thriller about a widowed child psychologist who lives in an isolated existence in rural New England. Caught in a deadly winter storm, she must find a way to rescue a young boy before he disappears forever.", 
    rating=4.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Shut In", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    