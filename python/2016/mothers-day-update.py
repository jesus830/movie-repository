
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Mother's Day", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Mother's Day", 
        year=2016, 
        plot="Three generations come together in the week leading up to Mother's Day.", 
        rating=5.6
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    