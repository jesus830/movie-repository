
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Indignation to the database
movies.insert(
    title="Indignation", 
    year=2016, 
    plot="In 1951, Marcus, a working-class Jewish student from New Jersey, attends a small Ohio college, where he struggles with sexual repression and cultural disaffection, amid the ongoing Korean War.", 
    rating=6.9
)

# Confirm that the movie was added
movie = movies.select(
    title="Indignation", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    