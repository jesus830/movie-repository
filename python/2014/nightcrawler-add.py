
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Nightcrawler to the database
movies.insert(
    title="Nightcrawler", 
    year=2014, 
    plot="When Louis Bloom, a con man desperate for work, muscles into the world of L.A. crime journalism, he blurs the line between observer and participant to become the star of his own story.", 
    rating=7.9
)

# Confirm that the movie was added
movie = movies.select(
    title="Nightcrawler", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    