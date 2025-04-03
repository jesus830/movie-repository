
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Norman: The Moderate Rise and Tragic Fall of a New York Fixer", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Norman: The Moderate Rise and Tragic Fall of a New York Fixer", 
        year=2016, 
        plot="Norman Oppenheimer is a small time operator who befriends a young politician at a low point in his life. Three years later, when the politician becomes an influential world leader, Norman's life dramatically changes for better and worse.", 
        rating=7.1
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    