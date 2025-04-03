
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Intouchables", 
    year=2011
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Intouchables", 
        year=2011, 
        plot="After he becomes a quadriplegic from a paragliding accident, an aristocrat hires a young man from the projects to be his caregiver.", 
        rating=8.6
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    