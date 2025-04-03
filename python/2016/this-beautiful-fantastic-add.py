
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add This Beautiful Fantastic to the database
movies.insert(
    title="This Beautiful Fantastic", 
    year=2016, 
    plot="A young woman who dreams of being a children's author makes an unlikely friendship with a cantankerous, rich old widower.", 
    rating=6.9
)

# Confirm that the movie was added
movie = movies.select(
    title="This Beautiful Fantastic", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    