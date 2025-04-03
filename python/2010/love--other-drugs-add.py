
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Love & Other Drugs to the database
movies.insert(
    title="Love & Other Drugs", 
    year=2010, 
    plot="A young woman suffering from Parkinson's befriends a drug rep working for Pfizer in 1990s Pittsburgh.", 
    rating=6.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Love & Other Drugs", 
    year=2010
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    