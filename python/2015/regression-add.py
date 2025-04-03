
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Regression to the database
movies.insert(
    title="Regression", 
    year=2015, 
    plot="A detective and a psychoanalyst uncover evidence of a satanic cult while investigating the rape of a young woman.", 
    rating=5.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Regression", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    