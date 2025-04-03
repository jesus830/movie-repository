
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Karate Kid to the database
movies.insert(
    title="The Karate Kid", 
    year=2010, 
    plot="Work causes a single mother to move to China with her young son; in his new home, the boy embraces kung fu, taught to him by a master.", 
    rating=6.2
)

# Confirm that the movie was added
movie = movies.select(
    title="The Karate Kid", 
    year=2010
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    