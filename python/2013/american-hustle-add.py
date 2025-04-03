
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add American Hustle to the database
movies.insert(
    title="American Hustle", 
    year=2013, 
    plot="A con man, Irving Rosenfeld, along with his seductive partner Sydney Prosser, is forced to work for a wild FBI agent, Richie DiMaso, who pushes them into a world of Jersey powerbrokers and mafia.", 
    rating=7.3
)

# Confirm that the movie was added
movie = movies.select(
    title="American Hustle", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    