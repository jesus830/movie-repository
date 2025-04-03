
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Let's Be Cops", 
    year=2014
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Let's Be Cops", 
        year=2014, 
        plot="Two struggling pals dress as police officers for a costume party and become neighborhood sensations. But when these newly-minted "heroes" get tangled in a real life web of mobsters and dirty detectives, they must put their fake badges on the line.", 
        rating=6.5
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    