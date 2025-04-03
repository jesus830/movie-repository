
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Tinker Tailor Soldier Spy", 
    year=2011
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Tinker Tailor Soldier Spy", 
        year=2011, 
        plot="In the bleak days of the Cold War, espionage veteran George Smiley is forced from semi-retirement to uncover a Soviet agent within MI6.", 
        rating=7.1
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    