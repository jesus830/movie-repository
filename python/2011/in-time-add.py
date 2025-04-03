
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add In Time to the database
movies.insert(
    title="In Time", 
    year=2011, 
    plot="In a future where people stop aging at 25, but are engineered to live only one more year, having the means to buy your way out of the situation is a shot at immortal youth. Here, Will Salas finds himself accused of murder and on the run with a hostage - a connection that becomes an important part of the way against the system.", 
    rating=6.7
)

# Confirm that the movie was added
movie = movies.select(
    title="In Time", 
    year=2011
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    