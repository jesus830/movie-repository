
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="300", 
    year=2006
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="300", 
        year=2006, 
        plot="King Leonidas of Sparta and a force of 300 men fight the Persians at Thermopylae in 480 B.C.", 
        rating=7.7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    