
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Indignation", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Indignation", 
        year=2016, 
        plot="In 1951, Marcus, a working-class Jewish student from New Jersey, attends a small Ohio college, where he struggles with sexual repression and cultural disaffection, amid the ongoing Korean War.", 
        rating=6.9
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    