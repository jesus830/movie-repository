
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add A Good Year to the database
movies.insert(
    title="A Good Year", 
    year=2006, 
    plot="A British investment broker inherits his uncle's chateau and vineyard in Provence, where he spent much of his childhood. He discovers a new laid-back lifestyle as he tries to renovate the estate to be sold.", 
    rating=6.9
)

# Confirm that the movie was added
movie = movies.select(
    title="A Good Year", 
    year=2006
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    