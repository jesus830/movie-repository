
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Other Boleyn Girl", 
    year=2008
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Other Boleyn Girl", 
        year=2008, 
        plot="Two sisters contend for the affection of King Henry VIII.", 
        rating=6.7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    