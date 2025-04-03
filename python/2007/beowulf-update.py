
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Beowulf", 
    year=2007
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Beowulf", 
        year=2007, 
        plot="The warrior Beowulf must fight and defeat the monster Grendel who is terrorizing Denmark, and later, Grendel's mother, who begins killing out of revenge.", 
        rating=6.2
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    