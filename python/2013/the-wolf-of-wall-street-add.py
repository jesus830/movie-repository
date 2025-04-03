
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Wolf of Wall Street to the database
movies.insert(
    title="The Wolf of Wall Street", 
    year=2013, 
    plot="Based on the true story of Jordan Belfort, from his rise to a wealthy stock-broker living the high life to his fall involving crime, corruption and the federal government.", 
    rating=8.2
)

# Confirm that the movie was added
movie = movies.select(
    title="The Wolf of Wall Street", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    