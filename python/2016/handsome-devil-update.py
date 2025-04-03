
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Handsome Devil", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Handsome Devil", 
        year=2016, 
        plot="Ned and Conor are forced to share a bedroom at their boarding school. The loner and the star athlete at this rugby-mad school form an unlikely friendship until it's tested by the authorities.", 
        rating=7.4
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    