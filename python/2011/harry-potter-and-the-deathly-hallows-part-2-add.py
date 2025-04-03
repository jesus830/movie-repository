
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Harry Potter and the Deathly Hallows: Part 2 to the database
movies.insert(
    title="Harry Potter and the Deathly Hallows: Part 2", 
    year=2011, 
    plot="Harry, Ron and Hermione search for Voldemort's remaining Horcruxes in their effort to destroy the Dark Lord as the final battle rages on at Hogwarts.", 
    rating=8.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Harry Potter and the Deathly Hallows: Part 2", 
    year=2011
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    