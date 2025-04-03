
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Divergent to the database
movies.insert(
    title="Divergent", 
    year=2014, 
    plot="In a world divided by factions based on virtues, Tris learns she's Divergent and won't fit in. When she discovers a plot to destroy Divergents, Tris and the mysterious Four must find out what makes Divergents dangerous before it's too late.", 
    rating=6.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Divergent", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    