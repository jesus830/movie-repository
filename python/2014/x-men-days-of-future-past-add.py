
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add X-Men: Days of Future Past to the database
movies.insert(
    title="X-Men: Days of Future Past", 
    year=2014, 
    plot="The X-Men send Wolverine to the past in a desperate effort to change history and prevent an event that results in doom for both humans and mutants.", 
    rating=8
)

# Confirm that the movie was added
movie = movies.select(
    title="X-Men: Days of Future Past", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    