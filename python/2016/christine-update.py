
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Christine", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Christine", 
        year=2016, 
        plot="The story of Christine Chubbuck, a 1970s TV reporter struggling with depression and professional frustrations as she tries to advance her career.", 
        rating=7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    