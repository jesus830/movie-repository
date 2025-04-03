
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Other Boleyn Girl to the database
movies.insert(
    title="The Other Boleyn Girl", 
    year=2008, 
    plot="Two sisters contend for the affection of King Henry VIII.", 
    rating=6.7
)

# Confirm that the movie was added
movie = movies.select(
    title="The Other Boleyn Girl", 
    year=2008
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    