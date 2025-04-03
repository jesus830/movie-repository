
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Lady Macbeth to the database
movies.insert(
    title="Lady Macbeth", 
    year=2016, 
    plot="Set in 19th century rural England, young bride who has been sold into marriage to a middle-aged man discovers an unstoppable desire within herself as she enters into an affair with a work on her estate.", 
    rating=7.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Lady Macbeth", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    