
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Teenage Mutant Ninja Turtles: Out of the Shadows to the database
movies.insert(
    title="Teenage Mutant Ninja Turtles: Out of the Shadows", 
    year=2016, 
    plot="After facing Shredder, who has joined forces with mad scientist Baxter Stockman and henchmen Bebop and Rocksteady to take over the world, the Turtles must confront an even greater nemesis: the notorious Krang.", 
    rating=6
)

# Confirm that the movie was added
movie = movies.select(
    title="Teenage Mutant Ninja Turtles: Out of the Shadows", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    