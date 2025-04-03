
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Help to the database
movies.insert(
    title="The Help", 
    year=2011, 
    plot="An aspiring author during the civil rights movement of the 1960s decides to write a book detailing the African American maids' point of view on the white families for which they work, and the hardships they go through on a daily basis.", 
    rating=8.1
)

# Confirm that the movie was added
movie = movies.select(
    title="The Help", 
    year=2011
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    