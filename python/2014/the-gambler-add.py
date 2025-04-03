
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Gambler to the database
movies.insert(
    title="The Gambler", 
    year=2014, 
    plot="Lit professor and gambler Jim Bennett's debt causes him to borrow money from his mother and a loan shark. Further complicating his situation is his relationship with one of his students. Will Bennett risk his life for a second chance?", 
    rating=6
)

# Confirm that the movie was added
movie = movies.select(
    title="The Gambler", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    