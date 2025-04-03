
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Harry Potter and the Deathly Hallows: Part 2", 
    year=2011
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Harry Potter and the Deathly Hallows: Part 2", 
        year=2011, 
        plot="Harry, Ron and Hermione search for Voldemort's remaining Horcruxes in their effort to destroy the Dark Lord as the final battle rages on at Hogwarts.", 
        rating=8.1
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    