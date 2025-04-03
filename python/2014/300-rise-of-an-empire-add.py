
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add 300: Rise of an Empire to the database
movies.insert(
    title="300: Rise of an Empire", 
    year=2014, 
    plot="Greek general Themistokles leads the charge against invading Persian forces led by mortal-turned-god Xerxes and Artemisia, vengeful commander of the Persian navy.", 
    rating=6.2
)

# Confirm that the movie was added
movie = movies.select(
    title="300: Rise of an Empire", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    