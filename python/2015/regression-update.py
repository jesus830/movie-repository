
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Regression", 
    year=2015
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Regression", 
        year=2015, 
        plot="A detective and a psychoanalyst uncover evidence of a satanic cult while investigating the rape of a young woman.", 
        rating=5.7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    