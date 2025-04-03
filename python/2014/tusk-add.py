
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Tusk to the database
movies.insert(
    title="Tusk", 
    year=2014, 
    plot="When podcaster Wallace Bryton goes missing in the backwoods of Manitoba while interviewing a mysterious seafarer named Howard Howe, his best friend Teddy and girlfriend Allison team with an ex-cop to look for him.", 
    rating=5.4
)

# Confirm that the movie was added
movie = movies.select(
    title="Tusk", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    