
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Sisters", 
    year=2015
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Sisters", 
        year=2015, 
        plot="Two sisters decide to throw one last house party before their parents sell their family home.", 
        rating=6
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    