
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Green Inferno", 
    year=2013
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Green Inferno", 
        year=2013, 
        plot="A group of student activists travels to the Amazon to save the rain forest and soon discover that they are not alone, and that no good deed goes unpunished.", 
        rating=5.4
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    