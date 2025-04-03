
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Ticket to the database
movies.insert(
    title="The Ticket", 
    year=2016, 
    plot="A blind man who regains his vision finds himself becoming metaphorically blinded by his obsession for the superficial.", 
    rating=5.4
)

# Confirm that the movie was added
movie = movies.select(
    title="The Ticket", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    