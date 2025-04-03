
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Argo to the database
movies.insert(
    title="Argo", 
    year=2012, 
    plot="Acting under the cover of a Hollywood producer scouting a location for a science fiction film, a CIA agent launches a dangerous operation to rescue six Americans in Tehran during the U.S. hostage crisis in Iran in 1980.", 
    rating=7.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Argo", 
    year=2012
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    