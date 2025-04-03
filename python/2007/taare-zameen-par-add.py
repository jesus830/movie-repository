
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Taare Zameen Par to the database
movies.insert(
    title="Taare Zameen Par", 
    year=2007, 
    plot="An eight-year-old boy is thought to be a lazy trouble-maker, until the new art teacher has the patience and compassion to discover the real problem behind his struggles in school.", 
    rating=8.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Taare Zameen Par", 
    year=2007
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    