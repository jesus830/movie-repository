
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Bad Moms to the database
movies.insert(
    title="Bad Moms", 
    year=2016, 
    plot="When three overworked and under-appreciated moms are pushed beyond their limits, they ditch their conventional responsibilities for a jolt of long overdue freedom, fun, and comedic self-indulgence.", 
    rating=6.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Bad Moms", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    