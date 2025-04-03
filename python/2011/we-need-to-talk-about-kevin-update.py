
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="We Need to Talk About Kevin", 
    year=2011
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="We Need to Talk About Kevin", 
        year=2011, 
        plot="Kevin's mother struggles to love her strange child, despite the increasingly vicious things he says and does as he grows up. But Kevin is just getting started, and his final act will be beyond anything anyone imagined.", 
        rating=7.5
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    