
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Easy A", 
    year=2010
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Easy A", 
        year=2010, 
        plot="A clean-cut high school student relies on the school's rumor mill to advance her social and financial standing.", 
        rating=7.1
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    