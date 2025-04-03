
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Cinderella to the database
movies.insert(
    title="Cinderella", 
    year=2015, 
    plot="When her father unexpectedly passes away, young Ella finds herself at the mercy of her cruel stepmother and her scheming step-sisters. Never one to give up hope, Ella's fortunes begin to change after meeting a dashing stranger.", 
    rating=7
)

# Confirm that the movie was added
movie = movies.select(
    title="Cinderella", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    