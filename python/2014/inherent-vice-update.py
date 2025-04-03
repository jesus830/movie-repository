
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Inherent Vice", 
    year=2014
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Inherent Vice", 
        year=2014, 
        plot="In 1970, drug-fueled Los Angeles private investigator Larry "Doc" Sportello investigates the disappearance of a former girlfriend.", 
        rating=6.7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    