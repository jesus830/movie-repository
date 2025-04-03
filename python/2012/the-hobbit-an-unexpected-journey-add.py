
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Hobbit: An Unexpected Journey to the database
movies.insert(
    title="The Hobbit: An Unexpected Journey", 
    year=2012, 
    plot="A reluctant hobbit, Bilbo Baggins, sets out to the Lonely Mountain with a spirited group of dwarves to reclaim their mountain home - and the gold within it - from the dragon Smaug.", 
    rating=7.9
)

# Confirm that the movie was added
movie = movies.select(
    title="The Hobbit: An Unexpected Journey", 
    year=2012
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    