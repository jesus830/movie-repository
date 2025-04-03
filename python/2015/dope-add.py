
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Dope to the database
movies.insert(
    title="Dope", 
    year=2015, 
    plot="Life changes for Malcolm, a geek who's surviving life in a tough neighborhood, after a chance invitation to an underground party leads him and his friends into a Los Angeles adventure.", 
    rating=7.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Dope", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    