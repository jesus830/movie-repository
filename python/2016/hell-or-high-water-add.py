
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Hell or High Water to the database
movies.insert(
    title="Hell or High Water", 
    year=2016, 
    plot="A divorced father and his ex-con older brother resort to a desperate scheme in order to save their family's ranch in West Texas.", 
    rating=7.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Hell or High Water", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    