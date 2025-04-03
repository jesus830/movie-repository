
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Shooter", 
    year=2007
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Shooter", 
        year=2007, 
        plot="A marksman living in exile is coaxed back into action after learning of a plot to kill the President. Ultimately double-crossed and framed for the attempt, he goes on the run to find the real killer and the reason he was set up.", 
        rating=7.2
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    