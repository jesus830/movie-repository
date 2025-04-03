
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Stanford Prison Experiment to the database
movies.insert(
    title="The Stanford Prison Experiment", 
    year=2015, 
    plot="Twenty-four male students out of seventy-five were selected to take on randomly assigned roles of prisoners and guards in a mock prison situated in the basement of the Stanford psychology building.", 
    rating=6.9
)

# Confirm that the movie was added
movie = movies.select(
    title="The Stanford Prison Experiment", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    