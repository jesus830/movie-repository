
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Sherlock Holmes: A Game of Shadows", 
    year=2011
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Sherlock Holmes: A Game of Shadows", 
        year=2011, 
        plot="Sherlock Holmes and his sidekick Dr. Watson join forces to outwit and bring down their fiercest adversary, Professor Moriarty.", 
        rating=7.5
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    