
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Danish Girl to the database
movies.insert(
    title="The Danish Girl", 
    year=2015, 
    plot="A fictitious love story loosely inspired by the lives of Danish artists Lili Elbe and Gerda Wegener. Lili and Gerda's marriage and work evolve as they navigate Lili's groundbreaking journey as a transgender pioneer.", 
    rating=7
)

# Confirm that the movie was added
movie = movies.select(
    title="The Danish Girl", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    