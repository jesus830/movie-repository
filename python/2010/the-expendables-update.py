
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Expendables", 
    year=2010
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Expendables", 
        year=2010, 
        plot="A CIA operative hires a team of mercenaries to eliminate a Latin dictator and a renegade CIA agent.", 
        rating=6.5
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    