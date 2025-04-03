
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Hot Fuzz to the database
movies.insert(
    title="Hot Fuzz", 
    year=2007, 
    plot="Exceptional London cop Nicholas Angel is involuntarily transferred to a quaint English village and paired with a witless new partner. While on the beat, Nicholas suspects a sinister conspiracy is afoot with the residents.", 
    rating=7.9
)

# Confirm that the movie was added
movie = movies.select(
    title="Hot Fuzz", 
    year=2007
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    