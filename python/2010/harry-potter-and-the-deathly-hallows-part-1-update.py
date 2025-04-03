
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Harry Potter and the Deathly Hallows: Part 1", 
    year=2010
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Harry Potter and the Deathly Hallows: Part 1", 
        year=2010, 
        plot="As Harry races against time and evil to destroy the Horcruxes, he uncovers the existence of three most powerful objects in the wizarding world: the Deathly Hallows.", 
        rating=7.7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    