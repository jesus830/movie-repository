
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Enchanted to the database
movies.insert(
    title="Enchanted", 
    year=2007, 
    plot="A young maiden in a land called Andalasia, who is prepared to be wed, is sent away to New York City by an evil queen, where she falls in love with a lawyer.", 
    rating=7.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Enchanted", 
    year=2007
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    