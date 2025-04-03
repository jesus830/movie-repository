
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Beyond the Gates", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Beyond the Gates", 
        year=2016, 
        plot="Two estranged brothers reunite at their missing father's video store and find a VCR board game dubbed 'Beyond The Gates' that holds a connection to their father's disappearance.", 
        rating=5.2
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    