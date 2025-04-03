
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="All We Had", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="All We Had", 
        year=2016, 
        plot="A mother struggles to make a better life for her daughter.", 
        rating=5.8
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    