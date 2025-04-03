
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="X-Men: Days of Future Past", 
    year=2014
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="X-Men: Days of Future Past", 
        year=2014, 
        plot="The X-Men send Wolverine to the past in a desperate effort to change history and prevent an event that results in doom for both humans and mutants.", 
        rating=8
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    