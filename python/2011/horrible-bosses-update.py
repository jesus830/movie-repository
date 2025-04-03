
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Horrible Bosses", 
    year=2011
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Horrible Bosses", 
        year=2011, 
        plot="Three friends conspire to murder their awful bosses when they realize they are standing in the way of their happiness.", 
        rating=6.9
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    