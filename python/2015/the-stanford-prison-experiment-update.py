
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Stanford Prison Experiment", 
    year=2015
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Stanford Prison Experiment", 
        year=2015, 
        plot="Twenty-four male students out of seventy-five were selected to take on randomly assigned roles of prisoners and guards in a mock prison situated in the basement of the Stanford psychology building.", 
        rating=6.9
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    