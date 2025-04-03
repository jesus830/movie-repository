
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Hellboy II: The Golden Army to the database
movies.insert(
    title="Hellboy II: The Golden Army", 
    year=2008, 
    plot="The mythical world starts a rebellion against humanity in order to rule the Earth, so Hellboy and his team must save the world from the rebellious creatures.", 
    rating=7
)

# Confirm that the movie was added
movie = movies.select(
    title="Hellboy II: The Golden Army", 
    year=2008
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    