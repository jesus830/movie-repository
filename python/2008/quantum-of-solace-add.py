
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Quantum of Solace to the database
movies.insert(
    title="Quantum of Solace", 
    year=2008, 
    plot="James Bond descends into mystery as he tries to stop a mysterious organization from eliminating a country's most valuable resource. All the while, he still tries to seek revenge over the death of his love.", 
    rating=6.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Quantum of Solace", 
    year=2008
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    