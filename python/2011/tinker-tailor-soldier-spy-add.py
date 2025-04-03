
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Tinker Tailor Soldier Spy to the database
movies.insert(
    title="Tinker Tailor Soldier Spy", 
    year=2011, 
    plot="In the bleak days of the Cold War, espionage veteran George Smiley is forced from semi-retirement to uncover a Soviet agent within MI6.", 
    rating=7.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Tinker Tailor Soldier Spy", 
    year=2011
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    