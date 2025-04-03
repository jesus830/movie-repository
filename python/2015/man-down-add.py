
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Man Down to the database
movies.insert(
    title="Man Down", 
    year=2015, 
    plot="In a post-apocalyptic America, former U.S. Marine Gabriel Drummer searches desperately for the whereabouts of his son, accompanied by his best friend and a survivor.", 
    rating=5.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Man Down", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    