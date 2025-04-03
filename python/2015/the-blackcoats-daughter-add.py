
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Blackcoat's Daughter to the database
movies.insert(
    title="The Blackcoat's Daughter", 
    year=2015, 
    plot="Two girls must battle a mysterious evil force when they get left behind at their boarding school over winter break.", 
    rating=5.6
)

# Confirm that the movie was added
movie = movies.select(
    title="The Blackcoat's Daughter", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    