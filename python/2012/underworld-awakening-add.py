
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Underworld Awakening to the database
movies.insert(
    title="Underworld Awakening", 
    year=2012, 
    plot="When human forces discover the existence of the Vampire and Lycan clans, a war to eradicate both species commences. The vampire warrior Selene leads the battle against humankind.", 
    rating=6.4
)

# Confirm that the movie was added
movie = movies.select(
    title="Underworld Awakening", 
    year=2012
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    