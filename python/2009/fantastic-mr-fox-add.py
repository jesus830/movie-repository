
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Fantastic Mr. Fox to the database
movies.insert(
    title="Fantastic Mr. Fox", 
    year=2009, 
    plot="An urbane fox cannot resist returning to his farm raiding ways and then must help his community survive the farmers' retaliation.", 
    rating=7.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Fantastic Mr. Fox", 
    year=2009
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    