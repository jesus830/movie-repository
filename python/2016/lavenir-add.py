
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add L'avenir to the database
movies.insert(
    title="L'avenir", 
    year=2016, 
    plot="A philosophy teacher soldiers through the death of her mother, getting fired from her job, and dealing with a husband who is cheating on her.", 
    rating=7.1
)

# Confirm that the movie was added
movie = movies.select(
    title="L'avenir", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    