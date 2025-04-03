
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Rambo to the database
movies.insert(
    title="Rambo", 
    year=2008, 
    plot="In Thailand, John Rambo joins a group of missionaries to venture into war-torn Burma, and rescue a group of Christian aid workers who were kidnapped by the ruthless local infantry unit.", 
    rating=7.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Rambo", 
    year=2008
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    