
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="L'odyssée", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="L'odyssée", 
        year=2016, 
        plot="Highly influential and a fearlessly ambitious pioneer, innovator, filmmaker, researcher and conservationist, Jacques-Yves Cousteau's aquatic adventure covers roughly thirty years of an inarguably rich in achievements life.", 
        rating=6.7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    