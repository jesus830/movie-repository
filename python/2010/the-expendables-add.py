
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Expendables to the database
movies.insert(
    title="The Expendables", 
    year=2010, 
    plot="A CIA operative hires a team of mercenaries to eliminate a Latin dictator and a renegade CIA agent.", 
    rating=6.5
)

# Confirm that the movie was added
movie = movies.select(
    title="The Expendables", 
    year=2010
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    