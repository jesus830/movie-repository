
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Hellboy II: The Golden Army", 
    year=2008
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Hellboy II: The Golden Army", 
        year=2008, 
        plot="The mythical world starts a rebellion against humanity in order to rule the Earth, so Hellboy and his team must save the world from the rebellious creatures.", 
        rating=7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    