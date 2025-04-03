
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Colonia to the database
movies.insert(
    title="Colonia", 
    year=2015, 
    plot="A young woman's desperate search for her abducted boyfriend that draws her into the infamous Colonia Dignidad, a sect nobody has ever escaped from.", 
    rating=7.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Colonia", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    