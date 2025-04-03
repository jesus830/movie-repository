
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Love, Rosie to the database
movies.insert(
    title="Love, Rosie", 
    year=2014, 
    plot="Rosie and Alex have been best friends since they were 5, so they couldn't possibly be right for one another...or could they? When it comes to love, life and making the right choices, these two are their own worst enemies.", 
    rating=7.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Love, Rosie", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    