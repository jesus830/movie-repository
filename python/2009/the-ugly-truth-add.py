
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Ugly Truth to the database
movies.insert(
    title="The Ugly Truth", 
    year=2009, 
    plot="A romantically challenged morning show producer is reluctantly embroiled in a series of outrageous tests by her chauvinistic correspondent to prove his theories on relationships and help ... See full summary »", 
    rating=6.5
)

# Confirm that the movie was added
movie = movies.select(
    title="The Ugly Truth", 
    year=2009
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    