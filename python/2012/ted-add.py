
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Ted to the database
movies.insert(
    title="Ted", 
    year=2012, 
    plot="John Bennett, a man whose childhood wish of bringing his teddy bear to life came true, now must decide between keeping the relationship with the bear or his girlfriend, Lori.", 
    rating=7
)

# Confirm that the movie was added
movie = movies.select(
    title="Ted", 
    year=2012
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    