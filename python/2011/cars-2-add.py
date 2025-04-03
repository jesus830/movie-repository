
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Cars 2 to the database
movies.insert(
    title="Cars 2", 
    year=2011, 
    plot="Star race car Lightning McQueen and his pal Mater head overseas to compete in the World Grand Prix race. But the road to the championship becomes rocky as Mater gets caught up in an intriguing adventure of his own: international espionage.", 
    rating=6.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Cars 2", 
    year=2011
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    