
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Let's Be Cops to the database
movies.insert(
    title="Let's Be Cops", 
    year=2014, 
    plot="Two struggling pals dress as police officers for a costume party and become neighborhood sensations. But when these newly-minted "heroes" get tangled in a real life web of mobsters and dirty detectives, they must put their fake badges on the line.", 
    rating=6.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Let's Be Cops", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    