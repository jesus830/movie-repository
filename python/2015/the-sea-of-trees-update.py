
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Sea of Trees", 
    year=2015
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Sea of Trees", 
        year=2015, 
        plot="A suicidal American befriends a Japanese man lost in a forest near Mt. Fuji and the two search for a way out.", 
        rating=5.9
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    