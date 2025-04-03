
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Knock Knock to the database
movies.insert(
    title="Knock Knock", 
    year=2015, 
    plot="A devoted father helps two stranded young women who knock on his door, but his kind gesture turns into a dangerous seduction and a deadly game of cat and mouse.", 
    rating=4.9
)

# Confirm that the movie was added
movie = movies.select(
    title="Knock Knock", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    