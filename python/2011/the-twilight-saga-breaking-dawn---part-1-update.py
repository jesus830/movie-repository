
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Twilight Saga: Breaking Dawn - Part 1", 
    year=2011
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Twilight Saga: Breaking Dawn - Part 1", 
        year=2011, 
        plot="The Quileutes close in on expecting parents Edward and Bella, whose unborn child poses a threat to the Wolf Pack and the towns people of Forks.", 
        rating=4.9
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    