
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Iron Man Three to the database
movies.insert(
    title="Iron Man Three", 
    year=2013, 
    plot="When Tony Stark's world is torn apart by a formidable terrorist called the Mandarin, he starts an odyssey of rebuilding and retribution.", 
    rating=7.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Iron Man Three", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    