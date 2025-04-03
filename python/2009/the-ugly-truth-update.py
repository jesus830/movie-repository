
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Ugly Truth", 
    year=2009
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Ugly Truth", 
        year=2009, 
        plot="A romantically challenged morning show producer is reluctantly embroiled in a series of outrageous tests by her chauvinistic correspondent to prove his theories on relationships and help ... See full summary »", 
        rating=6.5
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    