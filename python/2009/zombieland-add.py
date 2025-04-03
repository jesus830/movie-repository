
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Zombieland to the database
movies.insert(
    title="Zombieland", 
    year=2009, 
    plot="A shy student trying to reach his family in Ohio, a gun-toting tough guy trying to find the last Twinkie, and a pair of sisters trying to get to an amusement park join forces to travel across a zombie-filled America.", 
    rating=7.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Zombieland", 
    year=2009
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    