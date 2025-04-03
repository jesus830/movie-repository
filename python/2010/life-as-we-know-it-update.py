
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Life as We Know It", 
    year=2010
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Life as We Know It", 
        year=2010, 
        plot="Two single adults become caregivers to an orphaned girl when their mutual best friends die in an accident.", 
        rating=6.6
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    