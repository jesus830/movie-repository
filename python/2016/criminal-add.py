
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Criminal to the database
movies.insert(
    title="Criminal", 
    year=2016, 
    plot="In a last-ditch effort to stop a diabolical plot, a dead CIA operative's memories, secrets, and skills are implanted into a death-row inmate in hopes that he will complete the operative's mission.", 
    rating=6.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Criminal", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    