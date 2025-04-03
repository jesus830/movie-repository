
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add El secreto de sus ojos to the database
movies.insert(
    title="El secreto de sus ojos", 
    year=2009, 
    plot="A retired legal counselor writes a novel hoping to find closure for one of his past unresolved homicide cases and for his unreciprocated love with his superior - both of which still haunt him decades later.", 
    rating=8.2
)

# Confirm that the movie was added
movie = movies.select(
    title="El secreto de sus ojos", 
    year=2009
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    