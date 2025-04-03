
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="You Don't Mess with the Zohan", 
    year=2008
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="You Don't Mess with the Zohan", 
        year=2008, 
        plot="An Israeli Special Forces Soldier fakes his death so he can re-emerge in New York City as a hair stylist.", 
        rating=5.5
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    