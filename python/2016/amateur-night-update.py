
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Amateur Night", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Amateur Night", 
        year=2016, 
        plot="Guy Carter is an award-winning graduate student of architecture. He's got a beautiful wife and a baby on the way. The problem? He doesn't have "his ducks in a row," which only fuels his ... See full summary »", 
        rating=5
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    