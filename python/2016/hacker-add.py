
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Hacker to the database
movies.insert(
    title="Hacker", 
    year=2016, 
    plot="With the help of his new friends Alex Danyliuk turns to a life of crime and identity theft.", 
    rating=6.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Hacker", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    