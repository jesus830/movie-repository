
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Shooter to the database
movies.insert(
    title="Shooter", 
    year=2007, 
    plot="A marksman living in exile is coaxed back into action after learning of a plot to kill the President. Ultimately double-crossed and framed for the attempt, he goes on the run to find the real killer and the reason he was set up.", 
    rating=7.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Shooter", 
    year=2007
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    