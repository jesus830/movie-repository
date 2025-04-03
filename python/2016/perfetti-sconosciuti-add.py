
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Perfetti sconosciuti to the database
movies.insert(
    title="Perfetti sconosciuti", 
    year=2016, 
    plot="Seven long-time friends get together for a dinner. When they decide to share with each other the content of every text message, email and phone call they receive, many secrets start to unveil and the equilibrium trembles.", 
    rating=7.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Perfetti sconosciuti", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    