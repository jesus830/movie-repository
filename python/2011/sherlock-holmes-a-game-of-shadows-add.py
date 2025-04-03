
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Sherlock Holmes: A Game of Shadows to the database
movies.insert(
    title="Sherlock Holmes: A Game of Shadows", 
    year=2011, 
    plot="Sherlock Holmes and his sidekick Dr. Watson join forces to outwit and bring down their fiercest adversary, Professor Moriarty.", 
    rating=7.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Sherlock Holmes: A Game of Shadows", 
    year=2011
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    