
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Happening", 
    year=2008
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Happening", 
        year=2008, 
        plot="A science teacher, his wife, and a young girl struggle to survive a plague that causes those infected to commit suicide.", 
        rating=5
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    