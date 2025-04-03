
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Twilight Saga: Breaking Dawn - Part 1 to the database
movies.insert(
    title="The Twilight Saga: Breaking Dawn - Part 1", 
    year=2011, 
    plot="The Quileutes close in on expecting parents Edward and Bella, whose unborn child poses a threat to the Wolf Pack and the towns people of Forks.", 
    rating=4.9
)

# Confirm that the movie was added
movie = movies.select(
    title="The Twilight Saga: Breaking Dawn - Part 1", 
    year=2011
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    