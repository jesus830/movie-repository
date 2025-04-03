
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Kynodontas to the database
movies.insert(
    title="Kynodontas", 
    year=2009, 
    plot="Three teenagers live isolated, without leaving their house, because their over-protective parents say they can only leave when their dogtooth falls out.", 
    rating=7.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Kynodontas", 
    year=2009
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    