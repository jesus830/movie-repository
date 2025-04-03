
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Martian to the database
movies.insert(
    title="The Martian", 
    year=2015, 
    plot="An astronaut becomes stranded on Mars after his team assume him dead, and must rely on his ingenuity to find a way to signal to Earth that he is alive.", 
    rating=8
)

# Confirm that the movie was added
movie = movies.select(
    title="The Martian", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    