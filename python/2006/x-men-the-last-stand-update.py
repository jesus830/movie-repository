
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="X-Men: The Last Stand", 
    year=2006
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="X-Men: The Last Stand", 
        year=2006, 
        plot="When a cure is found to treat mutations, lines are drawn amongst the X-Men, led by Professor Charles Xavier, and the Brotherhood, a band of powerful mutants organized under Xavier's former ally, Magneto.", 
        rating=6.7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    