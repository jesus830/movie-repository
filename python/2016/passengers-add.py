
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Passengers to the database
movies.insert(
    title="Passengers", 
    year=2016, 
    plot="A spacecraft traveling to a distant colony planet and transporting thousands of people has a malfunction in its sleep chambers. As a result, two passengers are awakened 90 years early.", 
    rating=7
)

# Confirm that the movie was added
movie = movies.select(
    title="Passengers", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    