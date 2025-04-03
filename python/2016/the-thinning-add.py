
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Thinning to the database
movies.insert(
    title="The Thinning", 
    year=2016, 
    plot=""The Thinning" takes place in a post-apocalyptic future where population control is dictated by a high-school aptitude test. When two students (Logan Paul and Peyton List) discover the test... See full summary »", 
    rating=6
)

# Confirm that the movie was added
movie = movies.select(
    title="The Thinning", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    