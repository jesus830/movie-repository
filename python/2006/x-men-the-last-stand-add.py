
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add X-Men: The Last Stand to the database
movies.insert(
    title="X-Men: The Last Stand", 
    year=2006, 
    plot="When a cure is found to treat mutations, lines are drawn amongst the X-Men, led by Professor Charles Xavier, and the Brotherhood, a band of powerful mutants organized under Xavier's former ally, Magneto.", 
    rating=6.7
)

# Confirm that the movie was added
movie = movies.select(
    title="X-Men: The Last Stand", 
    year=2006
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    