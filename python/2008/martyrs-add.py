
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Martyrs to the database
movies.insert(
    title="Martyrs", 
    year=2008, 
    plot="A young woman's quest for revenge against the people who kidnapped and tormented her as a child leads her and a friend, who is also a victim of child abuse, on a terrifying journey into a living hell of depravity.", 
    rating=7.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Martyrs", 
    year=2008
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    