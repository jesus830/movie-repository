
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add G.I. Joe: The Rise of Cobra to the database
movies.insert(
    title="G.I. Joe: The Rise of Cobra", 
    year=2009, 
    plot="An elite military unit comprised of special operatives known as G.I. Joe, operating out of The Pit, takes on an evil organization led by a notorious arms dealer.", 
    rating=5.8
)

# Confirm that the movie was added
movie = movies.select(
    title="G.I. Joe: The Rise of Cobra", 
    year=2009
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    