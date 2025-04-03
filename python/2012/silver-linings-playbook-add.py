
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Silver Linings Playbook to the database
movies.insert(
    title="Silver Linings Playbook", 
    year=2012, 
    plot="After a stint in a mental institution, former teacher Pat Solitano moves back in with his parents and tries to reconcile with his ex-wife. Things get more challenging when Pat meets Tiffany, a mysterious girl with problems of her own.", 
    rating=7.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Silver Linings Playbook", 
    year=2012
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    