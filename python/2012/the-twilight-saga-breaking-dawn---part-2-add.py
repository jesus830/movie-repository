
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Twilight Saga: Breaking Dawn - Part 2 to the database
movies.insert(
    title="The Twilight Saga: Breaking Dawn - Part 2", 
    year=2012, 
    plot="After the birth of Renesmee, the Cullens gather other vampire clans in order to protect the child from a false allegation that puts the family in front of the Volturi.", 
    rating=5.5
)

# Confirm that the movie was added
movie = movies.select(
    title="The Twilight Saga: Breaking Dawn - Part 2", 
    year=2012
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    