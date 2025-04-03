
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Suicide Squad to the database
movies.insert(
    title="Suicide Squad", 
    year=2016, 
    plot="A secret government agency recruits some of the most dangerous incarcerated super-villains to form a defensive task force. Their first mission: save the world from the apocalypse.", 
    rating=6.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Suicide Squad", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    