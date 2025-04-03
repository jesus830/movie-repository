
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Fast & Furious", 
    year=2009
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Fast & Furious", 
        year=2009, 
        plot="Brian O'Conner, back working for the FBI in Los Angeles, teams up with Dominic Toretto to bring down a heroin importer by infiltrating his operation.", 
        rating=6.6
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    