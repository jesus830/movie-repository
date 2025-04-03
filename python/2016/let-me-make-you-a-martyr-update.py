
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Let Me Make You a Martyr", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Let Me Make You a Martyr", 
        year=2016, 
        plot="A cerebral revenge film about two adopted siblings who fall in love, and hatch a plan to kill their abusive father.", 
        rating=6.4
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    