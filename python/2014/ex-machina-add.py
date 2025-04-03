
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Ex Machina to the database
movies.insert(
    title="Ex Machina", 
    year=2014, 
    plot="A young programmer is selected to participate in a ground-breaking experiment in synthetic intelligence by evaluating the human qualities of a breath-taking humanoid A.I.", 
    rating=7.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Ex Machina", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    