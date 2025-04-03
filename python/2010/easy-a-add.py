
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Easy A to the database
movies.insert(
    title="Easy A", 
    year=2010, 
    plot="A clean-cut high school student relies on the school's rumor mill to advance her social and financial standing.", 
    rating=7.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Easy A", 
    year=2010
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    