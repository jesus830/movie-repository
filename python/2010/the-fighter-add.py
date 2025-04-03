
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Fighter to the database
movies.insert(
    title="The Fighter", 
    year=2010, 
    plot="A look at the early years of boxer "Irish" Micky Ward and his brother who helped train him before going pro in the mid 1980s.", 
    rating=7.8
)

# Confirm that the movie was added
movie = movies.select(
    title="The Fighter", 
    year=2010
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    