
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Book of Eli to the database
movies.insert(
    title="The Book of Eli", 
    year=2010, 
    plot="A post-apocalyptic tale, in which a lone man fights his way across America in order to protect a sacred book that holds the secrets to saving humankind.", 
    rating=6.9
)

# Confirm that the movie was added
movie = movies.select(
    title="The Book of Eli", 
    year=2010
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    