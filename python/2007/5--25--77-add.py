
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add 5- 25- 77 to the database
movies.insert(
    title="5- 25- 77", 
    year=2007, 
    plot="Alienated, hopeful-filmmaker Pat Johnson's epic story growing up in rural Illinois, falling in love, and becoming the first fan of the movie that changed everything.", 
    rating=7.1
)

# Confirm that the movie was added
movie = movies.select(
    title="5- 25- 77", 
    year=2007
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    