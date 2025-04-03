
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add White Girl to the database
movies.insert(
    title="White Girl", 
    year=2016, 
    plot="Summer, New York City. A college girl falls hard for a guy she just met. After a night of partying goes wrong, she goes to wild extremes to get him back.", 
    rating=5.8
)

# Confirm that the movie was added
movie = movies.select(
    title="White Girl", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    