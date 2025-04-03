
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Masterminds to the database
movies.insert(
    title="Masterminds", 
    year=2016, 
    plot="A guard at an armored car company in the Southern U.S. organizes one of the biggest bank heists in American history. Based on the October 1997 Loomis Fargo robbery.", 
    rating=5.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Masterminds", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    