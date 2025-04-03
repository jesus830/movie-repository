
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Harry Potter and the Deathly Hallows: Part 1 to the database
movies.insert(
    title="Harry Potter and the Deathly Hallows: Part 1", 
    year=2010, 
    plot="As Harry races against time and evil to destroy the Horcruxes, he uncovers the existence of three most powerful objects in the wizarding world: the Deathly Hallows.", 
    rating=7.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Harry Potter and the Deathly Hallows: Part 1", 
    year=2010
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    