
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Remember Me to the database
movies.insert(
    title="Remember Me", 
    year=2010, 
    plot="A romantic drama centered on two new lovers: Tyler, whose parents have split in the wake of his brother's suicide, and Ally, who lives each day to the fullest since witnessing her mother's murder.", 
    rating=7.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Remember Me", 
    year=2010
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    