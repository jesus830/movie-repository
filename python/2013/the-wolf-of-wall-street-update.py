
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Wolf of Wall Street", 
    year=2013
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Wolf of Wall Street", 
        year=2013, 
        plot="Based on the true story of Jordan Belfort, from his rise to a wealthy stock-broker living the high life to his fall involving crime, corruption and the federal government.", 
        rating=8.2
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    