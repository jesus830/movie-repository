
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Twilight Saga: Breaking Dawn - Part 2", 
    year=2012
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Twilight Saga: Breaking Dawn - Part 2", 
        year=2012, 
        plot="After the birth of Renesmee, the Cullens gather other vampire clans in order to protect the child from a false allegation that puts the family in front of the Volturi.", 
        rating=5.5
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    