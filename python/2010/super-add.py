
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Super to the database
movies.insert(
    title="Super", 
    year=2010, 
    plot="After his wife falls under the influence of a drug dealer, an everyday guy transforms himself into Crimson Bolt, a superhero with the best intentions, but lacking in heroic skills.", 
    rating=6.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Super", 
    year=2010
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    