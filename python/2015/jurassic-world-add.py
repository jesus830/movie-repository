
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Jurassic World to the database
movies.insert(
    title="Jurassic World", 
    year=2015, 
    plot="A new theme park, built on the original site of Jurassic Park, creates a genetically modified hybrid dinosaur, which escapes containment and goes on a killing spree.", 
    rating=7
)

# Confirm that the movie was added
movie = movies.select(
    title="Jurassic World", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    