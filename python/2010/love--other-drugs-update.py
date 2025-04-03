
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Love & Other Drugs", 
    year=2010
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Love & Other Drugs", 
        year=2010, 
        plot="A young woman suffering from Parkinson's befriends a drug rep working for Pfizer in 1990s Pittsburgh.", 
        rating=6.7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    