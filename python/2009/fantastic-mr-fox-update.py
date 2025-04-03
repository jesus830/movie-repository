
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Fantastic Mr. Fox", 
    year=2009
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Fantastic Mr. Fox", 
        year=2009, 
        plot="An urbane fox cannot resist returning to his farm raiding ways and then must help his community survive the farmers' retaliation.", 
        rating=7.8
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    