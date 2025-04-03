
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Bridget Jones's Baby to the database
movies.insert(
    title="Bridget Jones's Baby", 
    year=2016, 
    plot="Bridget's focus on single life and her career is interrupted when she finds herself pregnant, but with one hitch ... she can only be fifty percent sure of the identity of her baby's father.", 
    rating=6.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Bridget Jones's Baby", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    