
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="White Girl", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="White Girl", 
        year=2016, 
        plot="Summer, New York City. A college girl falls hard for a guy she just met. After a night of partying goes wrong, she goes to wild extremes to get him back.", 
        rating=5.8
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    