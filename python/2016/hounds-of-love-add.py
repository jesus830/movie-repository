
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Hounds of Love to the database
movies.insert(
    title="Hounds of Love", 
    year=2016, 
    plot="A cold-blooded predatory couple while cruising the streets in search of their next victim, will stumble upon a 17-year-old high school girl, who will be sedated, abducted and chained in the strangers' guest room.", 
    rating=6.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Hounds of Love", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    