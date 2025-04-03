
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Avengers to the database
movies.insert(
    title="The Avengers", 
    year=2012, 
    plot="Earth's mightiest heroes must come together and learn to fight as a team if they are to stop the mischievous Loki and his alien army from enslaving humanity.", 
    rating=8.1
)

# Confirm that the movie was added
movie = movies.select(
    title="The Avengers", 
    year=2012
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    