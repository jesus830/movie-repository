
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Paul", 
    year=2011
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Paul", 
        year=2011, 
        plot="Two British comic-book geeks traveling across the U.S. encounter an alien outside Area 51.", 
        rating=7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    