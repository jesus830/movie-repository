
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Annie to the database
movies.insert(
    title="Annie", 
    year=2014, 
    plot="A foster kid, who lives with her mean foster mom, sees her life change when business tycoon and New York mayoral candidate Will Stacks makes a thinly-veiled campaign move and takes her in.", 
    rating=5.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Annie", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    