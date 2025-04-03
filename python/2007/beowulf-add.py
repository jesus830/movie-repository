
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Beowulf to the database
movies.insert(
    title="Beowulf", 
    year=2007, 
    plot="The warrior Beowulf must fight and defeat the monster Grendel who is terrorizing Denmark, and later, Grendel's mother, who begins killing out of revenge.", 
    rating=6.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Beowulf", 
    year=2007
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    