
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Fast & Furious to the database
movies.insert(
    title="Fast & Furious", 
    year=2009, 
    plot="Brian O'Conner, back working for the FBI in Los Angeles, teams up with Dominic Toretto to bring down a heroin importer by infiltrating his operation.", 
    rating=6.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Fast & Furious", 
    year=2009
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    