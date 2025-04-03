
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Gunman to the database
movies.insert(
    title="The Gunman", 
    year=2015, 
    plot="A sniper on a mercenary assassination team, kills the minister of mines of the Congo. Terrier's successful kill shot forces him into hiding. Returning to the Congo years later, he becomes the target of a hit squad himself.", 
    rating=5.8
)

# Confirm that the movie was added
movie = movies.select(
    title="The Gunman", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    