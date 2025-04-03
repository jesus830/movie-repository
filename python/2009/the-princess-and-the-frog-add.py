
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Princess and the Frog to the database
movies.insert(
    title="The Princess and the Frog", 
    year=2009, 
    plot="A waitress, desperate to fulfill her dreams as a restaurant owner, is set on a journey to turn a frog prince back into a human being, but she has to face the same problem after she kisses him.", 
    rating=7.1
)

# Confirm that the movie was added
movie = movies.select(
    title="The Princess and the Frog", 
    year=2009
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    