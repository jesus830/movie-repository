
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Friends with Benefits to the database
movies.insert(
    title="Friends with Benefits", 
    year=2011, 
    plot="A young man and woman decide to take their friendship to the next level without becoming a couple, but soon discover that adding sex only leads to complications.", 
    rating=6.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Friends with Benefits", 
    year=2011
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    