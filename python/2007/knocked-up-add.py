
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Knocked Up to the database
movies.insert(
    title="Knocked Up", 
    year=2007, 
    plot="For fun-loving party animal Ben Stone, the last thing he ever expected was for his one-night stand to show up on his doorstep eight weeks later to tell him she's pregnant with his child.", 
    rating=7
)

# Confirm that the movie was added
movie = movies.select(
    title="Knocked Up", 
    year=2007
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    