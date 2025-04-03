
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add L'odyssée to the database
movies.insert(
    title="L'odyssée", 
    year=2016, 
    plot="Highly influential and a fearlessly ambitious pioneer, innovator, filmmaker, researcher and conservationist, Jacques-Yves Cousteau's aquatic adventure covers roughly thirty years of an inarguably rich in achievements life.", 
    rating=6.7
)

# Confirm that the movie was added
movie = movies.select(
    title="L'odyssée", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    