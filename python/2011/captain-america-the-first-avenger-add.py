
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Captain America: The First Avenger to the database
movies.insert(
    title="Captain America: The First Avenger", 
    year=2011, 
    plot="Steve Rogers, a rejected military soldier transforms into Captain America after taking a dose of a "Super-Soldier serum". But being Captain America comes at a price as he attempts to take down a war monger and a terrorist organization.", 
    rating=6.9
)

# Confirm that the movie was added
movie = movies.select(
    title="Captain America: The First Avenger", 
    year=2011
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    