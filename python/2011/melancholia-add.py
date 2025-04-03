
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Melancholia to the database
movies.insert(
    title="Melancholia", 
    year=2011, 
    plot="Two sisters find their already strained relationship challenged as a mysterious new planet threatens to collide with Earth.", 
    rating=7.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Melancholia", 
    year=2011
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    