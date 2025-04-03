
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Burnt to the database
movies.insert(
    title="Burnt", 
    year=2015, 
    plot="Adam Jones (Bradley Cooper) is a chef who destroyed his career with drugs and diva behavior. He cleans up and returns to London, determined to redeem himself by spearheading a top restaurant that can gain three Michelin stars.", 
    rating=6.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Burnt", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    