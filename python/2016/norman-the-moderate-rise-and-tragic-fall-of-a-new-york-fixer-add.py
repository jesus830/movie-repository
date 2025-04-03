
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Norman: The Moderate Rise and Tragic Fall of a New York Fixer to the database
movies.insert(
    title="Norman: The Moderate Rise and Tragic Fall of a New York Fixer", 
    year=2016, 
    plot="Norman Oppenheimer is a small time operator who befriends a young politician at a low point in his life. Three years later, when the politician becomes an influential world leader, Norman's life dramatically changes for better and worse.", 
    rating=7.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Norman: The Moderate Rise and Tragic Fall of a New York Fixer", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    