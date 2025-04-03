
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Giver to the database
movies.insert(
    title="The Giver", 
    year=2014, 
    plot="In a seemingly perfect community, without war, pain, suffering, differences or choice, a young boy is chosen to learn from an elderly man about the true pain and pleasure of the "real" world.", 
    rating=6.5
)

# Confirm that the movie was added
movie = movies.select(
    title="The Giver", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    