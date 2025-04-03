
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="5- 25- 77", 
    year=2007
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="5- 25- 77", 
        year=2007, 
        plot="Alienated, hopeful-filmmaker Pat Johnson's epic story growing up in rural Illinois, falling in love, and becoming the first fan of the movie that changed everything.", 
        rating=7.1
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    