
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Green Inferno to the database
movies.insert(
    title="The Green Inferno", 
    year=2013, 
    plot="A group of student activists travels to the Amazon to save the rain forest and soon discover that they are not alone, and that no good deed goes unpunished.", 
    rating=5.4
)

# Confirm that the movie was added
movie = movies.select(
    title="The Green Inferno", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    