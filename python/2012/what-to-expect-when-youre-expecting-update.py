
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="What to Expect When You're Expecting", 
    year=2012
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="What to Expect When You're Expecting", 
        year=2012, 
        plot="Follows the lives of five interconnected couples as they experience the thrills and surprises of having a baby, and realize that no matter what you plan for, life does not always deliver what is expected.", 
        rating=5.7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    