
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Kick-Ass 2 to the database
movies.insert(
    title="Kick-Ass 2", 
    year=2013, 
    plot="Following Kick-Ass' heroics, other citizens are inspired to become masked crusaders. But the Red Mist leads his own group of evil supervillains to kill Kick-Ass and destroy everything for which he stands.", 
    rating=6.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Kick-Ass 2", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    