
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add A Million Ways to Die in the West to the database
movies.insert(
    title="A Million Ways to Die in the West", 
    year=2014, 
    plot="As a cowardly farmer begins to fall for the mysterious new woman in town, he must put his new-found courage to the test when her husband, a notorious gun-slinger, announces his arrival.", 
    rating=6.1
)

# Confirm that the movie was added
movie = movies.select(
    title="A Million Ways to Die in the West", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    