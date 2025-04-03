
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Creed to the database
movies.insert(
    title="Creed", 
    year=2015, 
    plot="The former World Heavyweight Champion Rocky Balboa serves as a trainer and mentor to Adonis Johnson, the son of his late friend and former rival Apollo Creed.", 
    rating=7.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Creed", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    