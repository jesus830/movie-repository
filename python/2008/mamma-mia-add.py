
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Mamma Mia! to the database
movies.insert(
    title="Mamma Mia!", 
    year=2008, 
    plot="The story of a bride-to-be trying to find her real father told using hit songs by the popular '70s group ABBA.", 
    rating=6.4
)

# Confirm that the movie was added
movie = movies.select(
    title="Mamma Mia!", 
    year=2008
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    